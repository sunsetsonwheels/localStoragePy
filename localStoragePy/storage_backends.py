import os
import json
import stat
import pathlib
import shutil
import sqlite3


class localStoragePyStorageException(Exception):
    pass


class BasicStorageBackend:
    def __init__(self, app_namespace: str) -> None:
        # self.base_storage_path = os.path.join(pathlib.Path.home() , ".config", "localStoragePy")
        if app_namespace.count(os.sep) > 0:
            raise localStoragePyStorageException('app_namespace may not contain path separators!')
        self.app_storage_path = os.path.join(pathlib.Path.home() , ".config", "localStoragePy", app_namespace)
        if not os.path.isdir(self.app_storage_path):
            os.makedirs(os.path.join(self.app_storage_path))

    def raise_dummy_exception(self):
        raise localStoragePyStorageException("Called dummy backend!")

    def get_item(self, item: str) -> str:
        self.raise_dummy_exception()

    def set_item(self, item: str, value: any) -> None:
        self.raise_dummy_exception()

    def remove_item(self, item: str) -> None:
        self.raise_dummy_exception()

    def clear(self) -> None:
        self.raise_dummy_exception()
        

class TextStorageBackend(BasicStorageBackend):
    def __init__(self, app_namespace: str) -> None:
        super().__init__(app_namespace)

    def shutil_error_path(self, func, path, exc_info):
        if not os.access(path, os.W_OK):
            os.chmod(path, stat.S_IWUSR)
        func(path)

    def get_file_path(self, key: str) -> os.PathLike:
        return os.path.join(self.app_storage_path, key)

    def get_item(self, key: str) -> str:
        item_path = self.get_file_path(key)
        if os.path.isfile(item_path):
            with open(item_path, "r") as item_file:
                return str(item_file.read())
        else:
            return None

    def set_item(self, key: str, value: any) -> None:
        item_path = self.get_file_path(key)
        with open(item_path, "w") as item_file:
            item_file.write(str(value))

    def remove_item(self, key: str) -> None: 
        item_path = self.get_file_path(key)
        if os.path.isfile(item_path):
            os.remove(item_path)

    def clear(self) -> None:
        if os.path.isdir(self.app_storage_path):
            shutil.rmtree(self.app_storage_path, onerror=self.shutil_error_path)
        os.makedirs(self.app_storage_path)


class SQLiteStorageBackend(BasicStorageBackend):
    def __init__(self, app_namespace: str) -> None:
        super().__init__(app_namespace)
        self.db_path = os.path.join(self.app_storage_path, "localStorageSQLite.db")
        self.db_connection = sqlite3.connect(self.db_path)
        self.db_cursor = self.db_connection.cursor()

        empty = self.db_cursor.execute("SELECT name FROM sqlite_master").fetchall()
        if empty == []:
            self.create_default_tables()

    def create_default_tables(self) -> None:
        self.db_cursor.execute("CREATE TABLE localStoragePy (key TEXT PRIMARY KEY, value TEXT)")
        self.db_connection.commit()
        
    def get_item(self, key: str) -> str:
        fetched_value = self.db_cursor.execute("SELECT value FROM localStoragePy WHERE key = ?", (key,)).fetchone()
        if type(fetched_value) is tuple:
            return fetched_value[0]
        else:
            return None

    def set_item(self, key: str, value: any) -> None:
        if len(self.db_cursor.execute("SELECT key FROM localStoragePy WHERE key = ?", (key,)).fetchall()) == 0:
            self.db_cursor.execute("INSERT INTO localStoragePy (key, value) VALUES (?, ?)", (key, str(value)))
        else:
            self.db_cursor.execute("UPDATE localStoragePy SET value = ? WHERE key = ?", (str(value), key))
        self.db_connection.commit()

    def remove_item(self, key: str) -> None:
        self.db_cursor.execute("DELETE FROM localStoragePy WHERE key = ?", (key,))
        self.db_connection.commit()

    def clear(self) -> None:
        self.db_cursor.execute("DROP TABLE localStoragePy")
        self.create_default_tables()


class JSONStorageBackend(BasicStorageBackend):
    def __init__(self, app_namespace: str) -> None:
        super().__init__(app_namespace)
        self.json_path = os.path.join(self.app_storage_path, "localStorageJSON.json")
        self.json_data = {}

        if not os.path.isfile(self.json_path):
            self.commit_to_disk()

        with open(self.json_path, "r") as json_file:
            self.json_data = json.load(json_file)
        
    def commit_to_disk(self):
        with open(self.json_path, "w") as json_file:
            json.dump(self.json_data, json_file)

    def get_item(self, key: str) -> str:
        if key in self.json_data:
            return self.json_data[key]
        return None

    def set_item(self, key: str, value: any) -> None:
        self.json_data[key] = str(value)
        self.commit_to_disk()

    def remove_item(self, key: str) -> None: 
        self.json_data.pop(key)
        self.commit_to_disk()

    def clear(self) -> None:
        if os.path.isfile(self.json_path):
            os.remove(self.json_path)
        self.json_data = {}
        self.commit_to_disk()
    
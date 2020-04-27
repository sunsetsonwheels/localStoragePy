import os
import shutil
import stat
import pathlib

def onErrorPatch(self, func, path, exc_info):
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)
    func(path)

class localStoragePy:
    def __init__(self, appURL):
        if appURL.count(os.sep) > 0:
            raise TypeError('appURL may not contain path separators!')
        self.localStorageRoot = os.path.join(pathlib.Path.home() , ".localStorage")
        self.appLocalStorageRoot = os.path.join(self.localStorageRoot, appURL)
        if not os.path.isdir(self.localStorageRoot):
            os.mkdir(self.localStorageRoot)
        if not os.path.isdir(self.appLocalStorageRoot):
            os.mkdir(self.appLocalStorageRoot)
    def getItem(self, item):
        itemFile = os.path.join(self.appLocalStorageRoot, item)
        if os.path.isfile(itemFile):
            with open(itemFile, "r") as f:
                return str(f.read())
        else:
            return None
    def setItem(self, item, value):
        itemFile = os.path.join(self.appLocalStorageRoot, item)
        if os.path.isfile(itemFile):
            os.remove(itemFile)
        with open(itemFile, 'w') as f:
            f.write(str(value))
    def removeItem(self, item):
        itemFile = os.path.join(self.appLocalStorageRoot, item)
        if os.path.isfile(itemFile):
            os.remove(itemFile)
    def clear(self):
        if os.path.isdir(self.appLocalStorageRoot):
            shutil.rmtree(self.appLocalStorageRoot, onerror=onErrorPatch)
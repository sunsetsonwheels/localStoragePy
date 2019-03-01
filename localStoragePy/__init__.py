from os.path import isfile, isdir
from os import remove, mkdir, chmod, access, W_OK
from stat import S_IWUSR
from shutil import rmtree
from sys import platform
from pathlib import Path

def onErrorPatch(self, func, path, exc_info):
    if not access(path, W_OK):
        chmod(path, S_IWUSR)
    func(path)

class localStorage:
    def __init__(self, appURL):
        self.localStorageRoot = str(Path.home())+"/.localStorage"
        self.appLocalStorageRoot = self.localStorageRoot+"/"+appURL
        if not isdir(self.localStorageRoot):
            mkdir(self.localStorageRoot)
        if not isdir(self.appLocalStorageRoot):
            mkdir(self.appLocalStorageRoot)
    def getItem(self, item):
        itemFile = self.appLocalStorageRoot+"/"+item
        if isfile(itemFile):
            with open(itemFile, "r") as f:
                return f.read()
        else:
            return None
    def setItem(self, item, value):
        itemFile = self.appLocalStorageRoot+"/"+item
        if isfile(itemFile):
            remove(itemFile)
        with open(itemFile, 'w') as f:
            f.write(value)
    def removeItem(self, item):
        itemFile = self.appLocalStorageRoot+"/"+item
        if isfile(itemFile):
            remove(itemFile)
    def clear(self):
        if isdir(self.appLocalStorageRoot):
            rmtree(self.appLocalStorageRoot, onerror=onErrorPatch)
# localStoragePy
[![HitCount](http://hits.dwyl.io/jkelol111/localStorage.svg)](http://hits.dwyl.io/jkelol111/localStoragePy) ![PyPI](https://img.shields.io/pypi/v/localStoragePy.svg?style=flat-square) ![Travis (.org)](https://img.shields.io/travis/jkelol111/localStoragePy.svg?style=flat-square) ![GitHub issues](https://img.shields.io/github/issues-raw/jkelol111/localStoragePy.svg?style=flat-square) ![PyPI - License](https://img.shields.io/pypi/l/localStoragePy.svg?style=flat-square)

A familiar API from the Web, adapted to storing data locally with Python.

### Get started

1. Install using PyPi: `$ pip3 install localStoragePy`

2. Import into your project: `from localStoragePy import localStoragePy`

3. Setup localStorage: `localStorage = localStoragePy('your-app-namespace', 'your-storage-backend')` 

- `your-app-namespace`: whatever you want (example: `me.jkelol111.mypythonapp`) excluding path separators `/ \` or other disallowed characters in file name for your intended platform

- `your-storage-backend`: your preferred storage backend (`sqlite` by default).
    - Available storage backends:
        - `text`: text files for each storage item.
        - `sqlite`: a single database for all storage items.
        - `json`: a single JSON file for all storage items.

4. Use your typical localStorage syntax to store/read your strings:

- `localStorage.getItem(item)`

- `localStorage.setItem(item, value)`

- `localStorage.removeItem(item)`

- `localStorage.clear()`

*It's that familiar and simple.*

### When is this useful?

- When you want to store tiny strings for your app...

- Or your app's configuration in JSON...

Etcetra.

# localStoragePy
[![HitCount](http://hits.dwyl.io/jkelol111/localStorage.svg)](http://hits.dwyl.io/jkelol111/localStoragePy) ![PyPI](https://img.shields.io/pypi/v/localStoragePy.svg?style=flat-square)

A familiar API from the Web, adapted to storing data locally with Python.

### Get started

1. Install using PyPi: `$ pip3 install localStoragePy`

2. Import into your project: `from localStoragePy import localStorage as lc`

3. Setup localStorage: `localStorage = lc('your-app-url')` (replace `your-app-url` with whatever you want)

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

#!/usr/bin/env python3
from localStoragePy import localStoragePy
from pprint import pprint
from json import loads, dumps

storage_backend = "text"

def test():
    global storage_backend
    teststr = 'Hello World'
    testjson = {"testing": "Hello World"}
    print(f"[0/5] Initialize localStorage with storage backend: {storage_backend}.")
    localStorage = localStoragePy("testing.jkelol111.me", storage_backend)
    print("[1/5] setItem type str.")
    localStorage.setItem("testing_string", teststr)
    print("[2/5] setItem type str but it is JSON.")
    localStorage.setItem("testing_string_json", dumps(testjson))
    print("[3/5] getItem type str.")
    if localStorage.getItem('testing_string') == teststr:
        print(localStorage.getItem("testing_string"))
    else:
        raise NameError('testing_string')
    print("[4/5] getItem type str but it is JSON.")
    if loads(localStorage.getItem("testing_string_json"))['testing'] == testjson['testing']:
        pprint(loads(localStorage.getItem("testing_string_json")))
    print("[5/5] Clear all.")
    localStorage.clear()
    print("")

if __name__ == "__main__":
    print("Starting testing for localStoragePy...")
    print("")
    for backend in ["text", "sqlite", "json"]:
        storage_backend = backend
        test()
    print("Everything passed!")

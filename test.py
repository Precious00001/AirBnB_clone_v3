#!/usr/bin/python3
import importlib

app = importlib.import_module("api.v1.app")

print(app.__doc__)
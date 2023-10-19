import sys


def is_stdlib_module(module_name):
    return  module_name.split('.')[0] in _stdlib_modules


_stdlib_modules =  sys.stdlib_module_names

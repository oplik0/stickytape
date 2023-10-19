import sys


def is_stdlib_module(module_name):
    return any([module in _stdlib_modules for module in module_name.split('.')])


_stdlib_modules =  sys.stdlib_module_names

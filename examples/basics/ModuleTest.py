# from basics import BasicTutorials
# WILL import modules defined by __all__ from file __init__.py
from basics import *

if __name__ == "__main__":
    # The __name__ will be __main__ if script is run as (instead of import):
    # python ModuleTest.py <arguments>
    # Module search path
    # Built-in -> sys.path -> PYTHONPATH
    # Python Caches
    # *.pyc
    # Stan
    BasicTutorials.modules()
    import os, sys, builtins
    # dir() shows which names a module defines
    print(dir(sys))
    print(dir(builtins))
    print(sys.path)

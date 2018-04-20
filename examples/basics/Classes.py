
# Class -> new type of object consisting of [instance, methods]
# OOP + Multiple Inheritance
# Features:
#   default public members && all virtual methods && operator overload
#   built-in are objects

# Namespaces / Scopes ->
# Attributes:   O.attr
# Class triggers a new namespace
import logging


class Example1:
    """Class document is also an attribute [__doc__] of class"""
    # This is an attribute to Example1
    logger = logging.getLogger()

    # This is also an attribute to Example1
    def do_some_logging(self):
        # logger is not visible in this scope
        print("No logger access")


ex1 = Example1()
ex1.do_some_logging()





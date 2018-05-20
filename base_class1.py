#!/usr/bin/env python

from group_function1 import function1, function2


class MyBaseClass1(object):
    """
    A class to do some demo things
    """
    def __init__(self):
        self.default_var1 = "I am the init string in base class 1"
        self.var1 = self.default_var1
        function1()

    def get_base_string(self):
        return self.var1

    def set_base_string(self, new_string=None):
        if not new_string:
            new_string = self.default_var1
        self.var1 = new_string


class MyBaseClass2(object):
    """
    Another class to do some demo things
    """
    def __init__(self):
        self.var1 = "MyVariable"
        print("Do something cool here with " + self.var1)
        function2()

    def base_class2_function1(self):
        print("do something cooler here with " + self.var1)
        return

    def base_class2_function2(self):
        print("Do something even cooler here with " + self.var1)
        return

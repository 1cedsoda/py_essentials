# -*- coding: utf-8 -*-
# !/usr/bin/env python3


class ImportError(Exception):
    def __init__(self, fails):
        super(ImportError, self).__init__("You need to install the following packages:" + str(fails) + "\n" + " " * 24 + "$ pip3 install <package>")


class UnsupportedHashingAlgorythm(Exception):
    def __init__(self, function, algorythm, supported):
        super(ImportError, self).__init__("The", function, "do not support the", algorythm, ".\nSupported algorythms:", supported)


class StrangeError(Exception):
    def __init__(self, function, e):
        super(ImportError, self).__init__(function, "- An undefined error occured!\n", e)

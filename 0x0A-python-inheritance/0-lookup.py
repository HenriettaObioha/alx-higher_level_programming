#!/usr/bin/python 3

"""Function returns the list of available attributes and methods of an obj"""

def lookup(obj):
    """Returns list of available attributes"""
    return (dir(obj))

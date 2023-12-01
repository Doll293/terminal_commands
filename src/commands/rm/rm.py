"""Module providing a function that remove a file"""
import os


def remove(filename):
    if os.path.exists(filename):
        os.remove(filename)
        return True
    return False

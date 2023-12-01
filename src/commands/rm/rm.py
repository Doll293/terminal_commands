"""Module providing a function that removes a file"""
import os


def remove(filename):
    """function that removes a file"""
    if os.path.exists(filename):
        os.remove(filename)
        return True
    return False

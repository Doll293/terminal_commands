import os


def remove(filename):
    """function that remove a file"""
    if os.path.exists(filename):
        os.remove(filename)
        return True
    return False

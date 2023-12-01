import os


def remove(filename):
    if os.path.exists(filename):
        os.remove(filename)
        return True
    else:
        return False

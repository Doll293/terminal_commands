"""Module providing a function that creates a file"""


def touch(filename):
    """function that creates a file"""
    with open(filename, 'a', encoding="utf8") as file:
        file.close()

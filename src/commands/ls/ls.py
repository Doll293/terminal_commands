"""Module providing a function that lists files and subdirectories of the current directory"""
import os


def ls():
    """function that lists files and subdirectories of the current directory"""
    all_files_and_dir = [os.curdir, os.pardir]
    for dir_item in os.listdir():
        all_files_and_dir.append(dir_item)

    for el in all_files_and_dir:
        print(el)

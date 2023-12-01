"""Module providing a function that creates a file"""
import os


def touch(filename):
    # Ouvrir le fichier en mode append ('a') et immédiatement le fermer.
    file = open(filename, 'a')
    file.close()

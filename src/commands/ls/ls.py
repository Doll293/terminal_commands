import os


def ls():
    all_files_and_dir = []
    all_files_and_dir.append(os.curdir)
    all_files_and_dir.append(os.pardir)
    for dir in os.listdir():
        all_files_and_dir.append(dir)

    for el in all_files_and_dir:
        print(el)

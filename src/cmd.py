"""Main program"""
from commands.ls.ls import ls
from commands.rm.rm import remove
from commands.touch.touch import touch
import sys

while True:
    command = input("Enter command: ").strip().split()

    if len(command) == 0:
        continue

    if command[0] == "ls":
        ls()
    elif command[0] == "rm" and len(command) > 1:
        remove(command[1])
    elif command[0] == "touch" and len(command) > 1:
        touch(command[1])
    else:
        print("Unknown command or missing arguments.")
        sys.exit()


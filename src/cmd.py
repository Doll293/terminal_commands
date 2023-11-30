from commands.ls.ls import ls

while True:
    command = input()

    if command == "ls":
        ls()
    elif command != "ls":
        exit()
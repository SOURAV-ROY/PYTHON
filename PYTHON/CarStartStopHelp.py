command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("Car Start")
    elif command == "stop":
        print("Car Stop")
    elif command == "help":
        print("Start -> Start Car "
              "\nStop => Stop car "
              "\nQuit -> To Quit")
    elif command == "quit":
        break
    else:
        print("Sorry I don't Understand")

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car Already Started :)")
        else:
            started = True
            print("Car Start")
    elif command == "stop":
        if not started:
            print("Car Already Stopped :(")
        else:
            started = False
            print("Car Stop")
    elif command == "help":
        print("Start -> Start Car "
              "\nStop => Stop car "
              "\nQuit -> To Quit")
    elif command == "quit":
        break
    else:
        print("Sorry I don't Understand")

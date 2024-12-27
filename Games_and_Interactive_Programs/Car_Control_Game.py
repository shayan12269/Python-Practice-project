# Practice 17 | Car Control Game

# Initialize the car's status
car_started = False

while True:
    # Prompt the user for a command
    command = input("Enter command (type 'help' for options): ").lower()
    
    if command == "help":
        # Display available commands
        print(''' 
Available commands:
    start - to start the car
    stop  - to stop the car
    quit  - to exit
        ''')
    
    elif command == "start":
        if car_started:
            # Inform the user if the car is already started
            print("The car is already started.")
        else:
            # Start the car
            car_started = True
            print("Car started, ready to go.")
    
    elif command == "stop":
        if car_started:
            # Stop the car
            car_started = False
            print("Car stopped.")
        else:
            # Inform the user if the car is already stopped
            print("The car is already stopped.")
    
    elif command == "quit":
        # Exit the game
        print("Exiting the Car Control Game. Goodbye!")
        break
    
    else:
        # Handle unrecognized commands
        print("I don't understand that command...")

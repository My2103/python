# Define the Menu options
menu_options = ["Open", "Save", "Compile", "Run", "Quit"]

def printMenu(options):
    """Display the menu option"""
    index = 1
    for option in options:
        print(f"{index} {option}")
        index += 1

def acceptCommand(menu_length):
    """Accepts and validates the user's command."""
    while True:
        try: 
            command = int(input("Enter a number: "))
            if 1 <= command <= menu_length:
                return command
            else:
                print("Error: Input out of the range")
        except ValueError:
            print("Error: Please enter a valid number.")

def performCommand(command, options):
    """Performs the select command."""
    print(f"Command = {options[command - 1]}")

def main():
    """Main function the run the command intepreter."""
    while True:
        printMenu(menu_options)
        command = acceptCommand(len(menu_options))
        if menu_options[command - 1] == "Quit":
            print("Exiting the program.")
            break
        performCommand(command, menu_options)
        print() # Add a blank line for readability

if __name__ == "__main__":
    main()


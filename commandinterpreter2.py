def display_menu():
    print("1 Open")
    print("2 Save")
    print("3 Compile")
    print("4 Run")
    print("5 Quit")

def main():
    commands = ["Open", "Save", "Compile", "Run", "Quit"]
    while True:
        display_menu()
        choice = int(input("Enter a number: "))
        if 1 <= choice <= 5:
            print(f"Command = {commands[choice - 1]}\n")
            if choice == 5:
                break
        else:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

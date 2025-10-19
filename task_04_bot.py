from colorama import Fore, Style


def parse_input(user_input):
    """Parse user input into command and arguments."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    """Add a new contact to the contacts dictionary."""
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    """Change an existing contact's phone number."""
    name, phone = args
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    """Show the phone number of a contact."""
    name = args[0]
    phone = contacts.get(name, "Contact not found.")
    return phone


def show_all(contacts):
    """Show all contacts."""
    string_contacts = ""
    for name, phone in contacts.items():
        string_contacts += f"{name}: {phone}\n"
    return string_contacts.strip()


def main():
    """Main function to run the assistant bot."""
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print(
                f"{Fore.RED}\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
                f"!!!!!!!!!!! Invalid command !!!!!!!!!!\n"
                f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!{Style.RESET_ALL}\n"
                f"Available commands: {Fore.BLUE}hello, add, change, phone, "
                f"all, close, exit{Style.RESET_ALL}\n"
                f"Examples:\n"
                f"--------------------------------------\n"
                f"{Fore.GREEN}add John 1234567890\n"
                f"change John 0987654321\n"
                f"phone John\n"
                f"all\n"
                f"close{Style.RESET_ALL}\n"
                f"--------------------------------------"
                )


if __name__ == "__main__":
    main()

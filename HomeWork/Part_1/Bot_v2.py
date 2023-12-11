
MENU = """
    * Available commands:
        #1 or hello
        #2 or add
        #3 or change
        #4 or get
        #5 or all
        #6 or close or exit or bye
"""

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid input. Please provide name and phone number separated by space."
        except Exception as e:
            return f"An error occurred: {str(e)}"

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid input. Please provide name and phone number separated by space."
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def main():
    contacts = {}
    print("\nWelcome to the assistant bot!")
    print(MENU)
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "bye", "6"]:
            print("Good bye!")
            break
        elif command in ["hello", "1"]:
            print("\nHow can I help you?")
        elif command in ["add", "2"]:
            print(add_contact(args, contacts))
        elif command in ["change", "3"]:
            print(add_contact(args, contacts))
        elif command in ["get", "4"]:
            found_contact = False
            for name, phone in contacts.items():
                if args in (name.lower(), phone.lower()):
                    print(f"Contact: {name} - Phone Number: {phone}")
                    found_contact = True
            if not found_contact:
                print(f"Contact {', '.join(args)} not found.")
        elif command in ["all", "5"]:
            if len(contacts) > 0:
                for name, phone in contacts.items():
                    print(f"{name:<15} {phone:<100}")
            else:
                print("List of contacts is empty!")
        else:
            print("Invalid command.")

        print(MENU)


if __name__ == "__main__":
    main()

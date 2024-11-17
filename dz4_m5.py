def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Not enough arguments. Please provide both name and phone."
        except KeyError:
            return "This contact does not exist."
        except Exception as e:
            return f"An error occurred: {str(e)}"
    return inner

def parse_input(user_input):
    parts = user_input.split()
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Give me name and phone please.")
    name, phone = args
    contacts[name] = phone
    return "Contact added"

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Give me name and phone please.")
    name, phone = args
    if name not in contacts:
        raise KeyError(name)
    contacts[name] = phone
    return f"Contact {name} changed."

@input_error
def phone_username(args, contacts):
    if len(args) != 1:
        raise ValueError("Give me name, please.")
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError(name)

@input_error
def all_contacts(contacts):
    if not contacts:
        return "No contacts available."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            result = add_contact(args, contacts)
            print(result)
        elif command == "change":
            result = change_contact(args, contacts)
            print(result)
        elif command == "phone":
            result = phone_username(args, contacts)
            print(result)
        elif command == "all":
            result = all_contacts(contacts)
            print(result)
        else:
            print("Invalid command. Please enter a valid command.")

if __name__ == "__main__":
    main()

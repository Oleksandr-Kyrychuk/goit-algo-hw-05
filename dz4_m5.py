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
    name, phone = args  # Помилка буде автоматично оброблена, якщо args некоректні
    contacts[name] = phone
    return "Contact added"

@input_error
def change_contact(args, contacts):
    name, phone = args  # Аналогічно, декоратор обробить помилку
    contacts[name] = phone  # Якщо ключа немає, KeyError буде оброблено декоратором
    return f"Contact {name} changed."

@input_error
def phone_username(args, contacts):
    name = args[0]  # IndexError буде оброблено декоратором
    return contacts[name]  # Якщо контакту немає, KeyError буде оброблено декоратором

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

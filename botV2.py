def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            return "Enter the argument for the command"

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def all (args):
    contacts = []
    for i in args:
        contacts.append(' '.join(list(i)))
    return '\n'.join(contacts)

@input_error
def change_nummer(contacts, name, new_nummer):
    contacts[name] = new_nummer
    return 'Contact changed'

@input_error
def phone (contacts, user):
    new_list = [str(user), str(contacts[user])]
    return ' '.join(new_list)
    


def main():
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
        elif command == "all":
            print(all(contacts.items()))
        elif command == "change":
            print(change_nummer(contacts, *args))
        elif command == 'phone':
            print(phone(contacts, *args))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
contacts = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found!"
        except ValueError:
            return "Invalid input format!"
        except IndexError:
            return "Invalid input format!"
    return inner

@input_error
def handle_hello():
    return "How can I help you?"

@input_error
def handle_add(name, phone):
    contacts[name] = phone
    return "Contact added successfully!"

@input_error
def handle_change(name, phone):
    contacts[name] = phone
    return "Contact updated successfully!"

@input_error
def handle_phone(name):
    return contacts[name]

@input_error
def handle_show_all():
    if len(contacts) == 0:
        return "No contacts found!"
    else:
        output = ""
        for name, phone in contacts.items():
            output += f"{name}: {phone}\n"
        return output

def main():
    while True:
        user_input = input("> ").lower().split(" ", 1)
        command = user_input[0]
        if command == "hello":
            print(handle_hello())
        elif command == "add":
            try:
                name, phone = user_input[1].split(" ")
                print(handle_add(name, phone))
            except IndexError:
                print("Give me name and phone please")
        elif command == "change":
            try:
                name, phone = user_input[1].split(" ")
                print(handle_change(name, phone))
            except IndexError:
                print("Give me name and phone please")
        elif command == "phone":
            try:
                name = user_input[1]
                print(handle_phone(name))
            except IndexError:
                print("Enter user name")
        elif command == "show":
            if len(user_input) == 1 or user_input[1] == "all":
                print(handle_show_all())
            else:
                print("Invalid command")
        elif command == "good" and len(user_input) > 1 and user_input[1] in ["bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()

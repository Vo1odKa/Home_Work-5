from collections import UserDict

class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if str(phone) == old_phone:
                phone.value = new_phone
                break

    def __str__(self):
        result = f"Name: {self.name}\n"
        if self.phones:
            result += "Phones:\n"
            for phone in self.phones:
                result += f"- {phone}\n"
        return result

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[str(record.name)] = record

    def search_records(self, **kwargs):
        result = []
        for record in self.data.values():
            match = True
            for field, value in kwargs.items():
                if field == "phone":
                    phones = [str(phone) for phone in record.phones]
                    if value not in phones:
                        match = False
                        break
                else:
                    if str(getattr(record, field)) != value:
                        match = False
                        break
            if match:
                result.append(record)
        return result

def main():
    address_book = AddressBook()

    while True:
        user_input = input("> ").lower().split(" ", 1)
        command = user_input[0]

        if command == "hello":
            print("How can I help you?")

        elif command == "add":
            try:
                name, phone = user_input[1].split(" ")
                if name and phone:
                    record = Record(name)
                    record.add_phone(phone)
                    address_book.add_record(record)
                    print("Contact added successfully!")
                else:
                    print("Invalid input format!")
            except IndexError:
                print("Give me name and phone please")

        elif command == "change":
            try:
                name, phone = user_input[1].split(" ")
                if name and phone:
                    records = address_book.search_records(name=name)
                    if records:
                        for record in records:
                            record.edit_phone(record.phones[0].value, phone)
                        print("Contact updated successfully!")
                    else:
                        print("Contact not found!")
                else:
                    print("Invalid input format!")
            except IndexError:
                print("Give me name and phone please")

        elif command == "phone":
            try:
                name = user_input[1]
                if name:
                    records = address_book.search_records(name=name)
                    if records:
                        for record in records:
                            phones = [str(phone) for phone in record.phones]
                            print("\n".join(phones))
                    else:
                        print("Contact not found!")
                else:
                    print("Enter user name")
            except IndexError:
                print("Enter user name")

        elif command == "show":
            if len(user_input) == 1 or user_input[1] == "all":
                if address_book.data:
                    for record in address_book.data.values():
                        print(record)
                else:
                    print("No contacts found!")
            else:
                print("Invalid command")

        elif command == "good" and len(user_input) > 1 and user_input[1] in ["bye", "close", "exit"]:
            print("Good bye!")
            break

        else:
            print("Invalid command")

if __name__ == "__main__":
    main()

# Lab 8: Contact book using lists and dictionaries
# Each contact is a dictionary; all contacts are stored in a list.

contacts = []

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added.")

def search_contact():
    name = input("Enter name to search: ")
    for c in contacts:
        if c["name"].lower() == name.lower():
            print("Found ->", c["name"], c["phone"], c["email"])
            return
    print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")
    for c in contacts:
        if c["name"].lower() == name.lower():
            c["phone"] = input("New phone: ")
            c["email"] = input("New email: ")
            print("Contact updated.")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    for c in contacts:
        if c["name"].lower() == name.lower():
            contacts.remove(c)
            print("Contact deleted.")
            return
    print("Contact not found.")

def display_contacts():
    if len(contacts) == 0:
        print("No contacts available.")
    for c in contacts:
        print(c["name"], "|", c["phone"], "|", c["email"])

while True:
    print("\n1.Add  2.Search  3.Update  4.Delete  5.Display  6.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        display_contacts()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")

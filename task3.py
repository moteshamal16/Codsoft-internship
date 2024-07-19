contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    if name in contacts:
        print("This contact already exists.")
    else:
        contacts[name] = {'phone': phone, 'email': email}
        print("Contact added successfully.")

def delete_contact():
    name = input("Enter name: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("This contact does not exist.")

def update_contact():
    name = input("Enter name: ")
    if name in contacts:
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email address: ")
        contacts[name]['phone'] = phone
        contacts[name]['email'] = email
        print("Contact updated successfully.")
    else:
        print("This contact does not exist.")

def search_contact():
    name = input("Enter name: ")
    if name in contacts:
        print("Contact found:")
        print("Name:", name)
        print("Phone:", contacts[name]['phone'])
        print("Email:", contacts[name]['email'])
    else:
        print("Contact not found.")

def display_contacts():
    if not contacts:
        print("There are no contacts.")
    else:
        print("Contacts list: ")
        for name, info in contacts.items():
            print("Name:", name)
            print("Phone:", info['phone'])
            print("Email:", info['email'])
            print("--------------------")

# Main program loop
while True:
    print("\nContact Book Menu: ")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Update Contact")
    print("4. Search Contact")
    print("5. Display Contacts")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice (1-6): "))
        
        if choice == 1:
            add_contact()
        elif choice == 2:
            delete_contact()
        elif choice == 3:
            update_contact()
        elif choice == 4:
            search_contact()
        elif choice == 5:
            display_contacts()
        elif choice == 6:
            print("Exiting Contact Book!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")


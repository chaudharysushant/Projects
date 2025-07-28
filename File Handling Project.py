import csv

FILE_PATH = r'C:\Users\Sushant-Chaudhary\Desktop\Projects\contacts.csv'

def view_contacts():
    with open(FILE_PATH, 'r') as file:
        reader = csv.DictReader(file)
        for contact in reader:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}")

def add_contact():
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")

    with open(FILE_PATH, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone])
    print("Contact added")

def search_contacts():
    search_name = input("Enter name").lower()
    with open(FILE_PATH, 'r') as file:
        reader =csv.DictReader(file)
        found = False
        for contact in reader:
            if search_name in contact['name'].lower():
                print(f"Found: {contact}")
                found = True
        if not found:
            print("No contacts found with that name.")

def delete_contact():
    name_to_delete = input("Enter name to delete: ").lower()
    contacts = []

    with open(FILE_PATH, 'r') as file:
        reader = csv.DictReader(file)
        for contact in reader:
            if contact['name'].lower() != name_to_delete:
                contacts.append(contact)

    with open(FILE_PATH, 'w', newline='') as file:
        fieldnames = ['name', 'email', 'phone']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

    print("Contact deleted if existed.")

def main():
    while True:
        print("\nContact Manager")
        print("1. View contacts")
        print("2. Add contact")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            view_contacts()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == '__main__':
    main()
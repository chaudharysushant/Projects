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


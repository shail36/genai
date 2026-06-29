# import os
# from datetime import datetime

# #File location
# file_path = r'C:\Users\sagar\OneDrive\Documents'

# #Check if the file exists
# if os.path.exists(file_path):
#     print(f"The file at {file_path} exists.")


# for filename in os.listdir(file_path):
#     file = os.path.join(file_path, filename)
#     # checking if it is a file
#     if os.path.isfile(file):
#         print(f"File: {filename}")
#         timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Get current timestamp
#         new_file_path = os.path.join(file_path, f"{filename}_{timestamp}.txt")  # Append timestamp to the filename
#         os.rename(file, new_file_path)
#         print(f"Renamed {filename} to {new_file_path}")

#-------------------------------------------

# import csv


# with open("employees.csv", "r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         if (int(row['Salary']) > 50000):
#             with open("high_salary_employees.csv", "a", newline="") as high_salary_file:
#                 writer = csv.DictWriter(high_salary_file, fieldnames=["ID", "Name", "Role", "City", "Salary"])
#                 if high_salary_file.tell() == 0:  # Check if file is empty to write header
#                     writer.writeheader()
#                 writer.writerow(row)
#         else:
#             print("Salary not eligible")

#-------------------------------------------

# import string


# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# operation = input("Choose an operation (+, -, *, /): ")

# if num1 < 0 or num2 < 0:
#     print("Negative numbers are not allowed.")
#     exit()

# if operation not in ["+", "-", "*", "/"]:
#     print("Invalid operation. Please choose from +, -, *, /.")
#     exit()

# if operation == "/" and num2 == 0:
#     print("Division by zero is not allowed.")
#     exit()


# if operation == "+":
#     result = num1 + num2
# elif operation == "-":
#     result = num1 - num2
# elif operation == "*":
#     result = num1 * num2
# elif operation == "/":
#     result = num1 / num2

# print(f"The result is: {result}")

#--------------------------------------------------

import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f)

def contact_book():
    contacts = load_contacts()
    Operation = input("Choose an operation: add, view, or exit: ").lower()
    if Operation == "add":
        while True:
            name = input("Enter contact name (or 'exit' to quit): ")
            if name.lower() == 'exit':
                break
            phone = input("Enter contact phone number: ")
            contacts[name] = phone
            goto = input("Do you want to add another contact? (yes/no): ").lower()
            if goto != 'yes':
                print("Contact Book:")
                for name, phone in contacts.items():
                    print(f"{name}: {phone}")
                break
    elif Operation == "view":
        print("Contact Book:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

    save_contacts(contacts)

contact_book()

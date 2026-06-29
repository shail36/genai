# # def order_summary(*args, **kwargs):
# #     '''This function takes a variable number of positional arguments (items ordered) 
# #     and keyword arguments (customer details) and prints a summary of the order.'''
# #     print("Items Ordered:")
# #     for item in args:
# #         print("-", item)

# #     print("\nCustomer Details:")
# #     for key, value in kwargs.items():
# #         print(f"{key}: {value}")

# # # Example usage
# # order_summary("Laptop", "Mouse", "Keyboard","USB","Charger",
# #               name="Shashank", city="Mumbai", payment_method="Credit Card", delivery="Express", contact="9876543210")

# # help(order_summary)

# # # Global variable
# # count = 0

# # def call_counter():
# #     global count   # tells Python we want to use the global variable
# #     count += 1     # update global variable
# #     message = "Function has been called"  # local variable
# #     print(message, count, "times")

# # # Example usage
# # call_counter()
# # call_counter()
# # call_counter()

# # print("Final count outside function:", count)

# # def reset_counter():
# #     global count
# #     count = 0
# #     print("Counter reset to zero.", count)

# # reset_counter()

# # Global variable to track employee count
# employee_count = 0

# def add_employee(name, role="Developer", *skills, **details):
#     """
#     Adds a new employee to the system.

#     Parameters:
#     name (str): Employee's name
#     role (str, optional): Employee's role (default is "Developer")
#     *skills: Flexible list of skills (positional arguments)
#     **details: Flexible keyword arguments for extra info (e.g., city, experience)

#     Returns:
#     str: Confirmation message with employee details
#     """
#     global employee_count
#     employee_count += 1  # update global counter

#     print(f"\nEmployee #{employee_count}")
#     print("Name:", name)
#     print("Role:", role)

#     if skills:
#         print("Skills:", ", ".join(skills))

#     if details:
#         print("Other Details:")
#         for key, value in details.items():
#             print(f"  {key}: {value}")

#     return f"Employee {name} added successfully!"

# # Example usage
# # Global counter
# employee_count = 0

# # Function to create employee record
# def add_employee(name, role="Developer", *skills, **details):
#     global employee_count
#     employee_count += 1
#     return {
#         "id": employee_count,
#         "name": name,
#         "role": role,
#         "skills": skills,
#         "details": details
#     }

# # Store employees in a list
# employees = []

# # Add multiple employees
# employees.append(add_employee("Shashank", "Mainframe Developer", "Python", "SQL", city="Mumbai", experience=7))
# employees.append(add_employee("Rahul", "AI Engineer", "TensorFlow", "PyTorch", city="Pune", experience=3))

# # Print results
# print("\nTotal employees in system:", employee_count)
# print("Employee Data List:")
# for emp in employees:
#     print(emp)


# # def fetch_employee_data(employee_id, *args, **kwargs):
# #     """
# #     Fetches employee data based on provided ID and optional parameters.

# #     Parameters:
# #     employee_id (int): Unique identifier for the employee
# #     *args: Flexible list of data fields to fetch (e.g., name, role)
# #     **kwargs: Flexible keyword arguments for filters (e.g., department, city)

# #     Returns:
# #     str: Simulated employee data based on input parameters
# #     """
# #     print(f"\nFetching data for Employee ID: {employee_id}")

# #     if args:
# #         print("Requested Data Fields:", ", ".join(args))

# #     if kwargs:
# #         print("Applied Filters:")
# #         for key, value in kwargs.items():
# #             print(f"  {key}: {value}")

# #     # Simulated data retrieval (in a real application, this would query a database)
# #     return f"Data for Employee ID {employee_id} fetched successfully!"

# # fetch_result = fetch_employee_data(101, "name", "role", department="IT", city="Mumbai")
# # print(fetch_result)

# # def calculate_salary(base_salary, bonuses):
# #     total_salary = base_salary + bonuses
# #     return total_salary

# # def employee_details(name, age, department):
# #     return f"Employee Name: {name}, Age: {age}, Department: {department}"

# # empoyee_info = employee_details("Shashank", 30, "IT")
# # print(empoyee_info)
# # employee_salary = calculate_salary(50000,5000)
# # print("Total Salary:", employee_salary)

# # def reset_employee_count():
# #     global employee_count
# #     employee_count = 0
# #     print("Employee count reset to zero.")



# import csv

# # Data to write
# employees = [
#     ["Name", "Role", "City", "Experience"],   # header row
#     ["Shashank", "Mainframe Developer", "Mumbai", 7],
#     ["Rahul", "AI Engineer", "Pune", 3],
#     ["Keshaw", "Tester", "Delhi", 2],
#     ["Anita", "Data Scientist", "Bangalore", 5]
# ]

# # Writing CSV file
# with open("employees.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(employees)

# print("CSV file created successfully!")

# import csv

# with open("employees.csv", "r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
# try:
#     with open("employees.csv", "r") as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError:
#     print("Oops! The file does not exist.")


employee_count = 0

def calculate_salary(base, bonus=5000):
    """Calculate total salary with base and optional bonus."""
    return base + bonus

def add_employee(name, role="Developer", *skills, **details):
    """Add an employee with flexible skills and details."""
    global employee_count
    employee_count += 1
    return {
        "id": employee_count,
        "name": name,
        "role": role,
        "skills": skills,
        "details": details
    }

# Step 1: Add employees
employees = []
employees.append(add_employee("Shashank", "Mainframe Developer", "Python", "SQL", city="Mumbai", experience=7))
employees.append(add_employee("Rahul", "AI Engineer", "TensorFlow", "PyTorch", city="Pune", experience=3))

# Step 2: Write to file
with open("employees.txt", "w") as f:
    for emp in employees:
        f.write(f"{emp['name']},{emp['role']},{emp['details']['city']}\n")

# Step 3: Read file back
with open("employees.txt", "r") as f:
    for line in f:
        print(line.strip())

# Step 4: Append new employee
employees.append(add_employee("Anita", "Data Scientist", "R", "Machine Learning", city="Bangalore", experience=5))
with open("employees.txt", "a") as f:
    f.write(f"{employees[-1]['name']},{employees[-1]['role']},{employees[-1]['details']['city']}\n")

# Step 5: Read CSV manually
# with open("employees.txt", "r") as f:
#     for line in f:
#         parts = line.strip().split(",")
#         print("Name:", parts[0], "| Role:", parts[1], "| City:", parts[2])

print(employees)
print("\nTotal employees in system:", employee_count)

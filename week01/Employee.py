import csv

# Define employee data
employees = [
    {"ID": 1, "Name": "Shashank", "Role": "Mainframe Developer", "City": "Mumbai", "Salary": 70000},
    {"ID": 2, "Name": "Rahul", "Role": "AI Engineer", "City": "Pune", "Salary": 85000},
    {"ID": 3, "Name": "Anita", "Role": "Data Scientist", "City": "Bangalore", "Salary": 95000},
    {"ID": 4, "Name": "Priya", "Role": "Web Developer", "City": "Delhi", "Salary": 60000},
    {"ID": 5, "Name": "Arjun", "Role": "System Analyst", "City": "Hyderabad", "Salary": 55000},
    {"ID": 6, "Name": "Meera", "Role": "UI Designer", "City": "Chennai", "Salary": 40000},
    {"ID": 7, "Name": "Vikram", "Role": "DevOps Engineer", "City": "Pune", "Salary": 75000},
    {"ID": 8, "Name": "Sneha", "Role": "QA Tester", "City": "Kolkata", "Salary": 30000},
    {"ID": 9, "Name": "Ravi", "Role": "Database Admin", "City": "Jaipur", "Salary": 65000},
    {"ID": 10, "Name": "Kiran", "Role": "Support Engineer", "City": "Lucknow", "Salary": 20000},
]

# Write to CSV file
with open("employees.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["ID", "Name", "Role", "City", "Salary"])
    writer.writeheader()
    writer.writerows(employees)

print("CSV file 'employees.csv' created successfully with 10 records.")

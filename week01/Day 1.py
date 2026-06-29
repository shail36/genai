# Convert string to int

num = str(42)
print(num)   # 50

# Convert int to string
age = 30
print("I am " + str(age) + " years old")
print(f"I am {age} years old")   # Using f-string for better readability

intro = "My name is \"Shashank\"" # Using escape character to include double quotes in the string
print(intro)

full_intro = intro + ''' I am 
30 years old.'''  # Using triple quotes to create a multi-line string
print(full_intro)

trim_intro = full_intro[28:41]  # Slicing the string to get a substring
print("trim intro")      
print(trim_intro)   # Output: name

# Convert string to float
pi = float("3.14159")
print(pi * 2)    # 6.28318

# Convert list to set
fruits = ["apple", "banana", "apple"]
unique_fruits = set(fruits)
print(unique_fruits)   # {'apple', 'banana'}

num=150
if 1 <= num <= 100:
    print("Number is between 1 and 100")
elif num > 100 or num < 1:
    print("Number is out of range")

nums = [1, 2, 3, 4, 5]

for n in nums:
    if n == 3:
        break      # stop loop at 3
    print(n)

for n in nums:
    if n % 2 == 0:
        continue   # skip even numbers
    print(n)

for n in nums:
    pass           # placeholder, does nothing

l=["Amit", "Riya", "Sam"]
for name in l:
    print(name)
# Simple Login System

# Predefined username and password
correct_username = "pogi"
correct_password = "ako"

# Prompt the user for input
username = input("Enter username: ")
password = input("Enter password: ")

# Check if the entered username and password are correct
if username == correct_username and password == correct_password:
    print("Login successful! Welcome!")
else:
    print("Invalid username or password. Please try again.")

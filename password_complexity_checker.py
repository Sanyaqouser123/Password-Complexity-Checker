import re  # Import the 're' module to use regular expressions

# Take input from the user
password = input("Enter your password: ")

# Check if password length is less than 8 characters
if len(password) < 8:
    print("Password must be at least 8 characters long.")

# Check if there is at least one uppercase letter
elif not re.search("[A-Z]", password):
    print("Password must contain at least 1 uppercase letter.")

# Check if there is at least one lowercase letter
elif not re.search("[a-z]", password):
    print("Password must contain at least 1 lowercase letter.")

# Check if there is at least one special character
elif not re.search("[!@#$%^&*()-_=+[\]{};:/?.>]", password):  # Make sure to escape brackets in the regex
    print("Password must contain at least 1 special character.")

# Check if there is at least one digit
elif not re.search("[0-9]", password): 
    print("Password must contain at least 1 number.") 

# If all checks are passed, the password is strong
else:
    print("Password is strong.")
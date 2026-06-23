import random
import string

print("=== Password Generator ===")

# Get password length from user
length = int(input("Enter password length: "))

# Define character sets
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = lowercase + uppercase + numbers + symbols

# Generate password
password = ""

for i in range(length):
    password += random.choice(all_characters)

# Display password
print("\nGenerated Password:")
print(password)
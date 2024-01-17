#Password Generator Project
# import random module
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password: ")) 
nr_symbols = int(input("How many symbols would you like: "))
nr_numbers = int(input("How many numbers would you like: "))

# Easy level
password = ""

# for loops
for char in range(0, nr_letters):
  password += random.choice(letters)

for char in range(0, nr_symbols):
  password += random.choice(symbols)

for char in range(0, nr_numbers):
  password += random.choice(numbers)

print(f"Here's your password (weak): {password}")


# Hard level
password_list = []

# for loops
for char in range(0, nr_letters):
  password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
  password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
  password_list.append(random.choice(numbers))
  
# Change the order of items in password_list
# using the random.shuffle()
random.shuffle(password_list)

# print(f"Here's your password: {password_list}")

# for loop to print it like an string text instead of a list items
password = ""
for char in password_list:
  password += char
print(f"Here's your password (strong): {password}")
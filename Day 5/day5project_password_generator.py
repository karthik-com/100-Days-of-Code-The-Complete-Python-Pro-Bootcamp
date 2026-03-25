## Project - Password Generator

# Solution - 

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = ""

# For easy passwords
for l in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password += random_char
for s in range(1, nr_symbols + 1):
    random_sym = random.choice(symbols)
    password += random_sym
for n in range(1, nr_numbers + 1):
    random_num = random.choice(numbers)
    password += random_num

print(f"Your easy password is: {password}")

#  For hard passwords

password_list = []

for let in range(0, nr_letters):
    random_let = random.choice(letters)
    password_list.append(random_let)
for sym in range(0, nr_symbols):
    random_sym = random.choice(symbols)
    password_list.append(random_sym)
for num in range(0, nr_numbers):
    random_num = random.choice(numbers)
    password_list.append(random_num)

random.shuffle(password_list)

password1 = ""
for new in password_list:
    password1 += new

print(f"Your hard password is: {password1}")




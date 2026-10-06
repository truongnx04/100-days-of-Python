import random

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

letter = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

print("Welcome to the PyPassword Generator!")
number_letters = int(input("How many letters would you like in your password?\n"))
number_symbols = int(input("How many symbols would you like?\n"))
number_numbers = int(input("How many numbers would you like?\n"))

password = ""

for char in range(0, number_letters):
    password += random.choice(letter)

for char in range(0, number_symbols):
    password += random.choice(symbol)

for char in range(0, number_numbers):
    password += random.choice(number)

list_password = list(password) # từ string sang list
random.shuffle(list_password) # tráo đổi vị trí trong list
text_shuffle = "".join(list_password) # kết nối list thành string

print(f"Your password is: {text_shuffle}")
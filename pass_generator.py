# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)


# Eazy Level - Order not randomised:

password = ""

for ch in range(1, nr_letters + 1):
    password += random.choice(letters)

for ch in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for ch in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(password)

#   Hard Level
password_lst = []

for ch in range(1, nr_letters + 1):
    password_lst.append(random.choice(letters))

for ch in range(1, nr_symbols + 1):
    password_lst.append(random.choice(symbols))

for ch in range(1, nr_numbers + 1):
    password_lst.append(random.choice(numbers))

random.shuffle(password_lst)
print("".join(password_lst))

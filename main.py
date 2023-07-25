import random
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '*', '&', '^', '_', '-', '(', ')']
password = []
random_password = ""

letters_num = int(input("Enter the number of letters you want\n"))
numbers_num = int(input("Enter the number of numbers you want\n"))
symbols_num = int(input("Enter the number of symbols you want\n"))


for item in range(1, letters_num + 1):
    password.append(random.choice(letters))

for item in range(1, numbers_num + 1):
    password.append(random.choice(numbers))

for item in range(1, symbols_num + 1):
    password.append(random.choice(symbols))

random.shuffle(password)

for item in password:
    random_password += item

print(f"Your password is : {random_password}")
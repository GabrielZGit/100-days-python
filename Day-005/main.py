import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

final_storage_password = []

for passletters in range (nr_letters):
    letters_selected = random.choice(letters)
    final_storage_password.append(letters_selected)

for passsymbols in range (nr_symbols):
    symbols_selected = random.choice(symbols)
    final_storage_password.append(symbols_selected)

for passnumbers in range (nr_numbers):
    numbers_selected = random.choice(numbers)
    final_storage_password.append(numbers_selected)

print(final_storage_password)

random.shuffle(final_storage_password)
print(final_storage_password)

my_final_password = "".join(final_storage_password)
print(my_final_password)




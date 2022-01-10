import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

letters_index = [] #this list will hold the letters
for letteri in range(nr_letters):
  random_index_let = random.randint(0, len(letters) - 1)
  letters_index.append(letters[random_index_let])
# print(letters_index)

symbols_index = [] #this list will hold the symbols
for symboli in range(nr_symbols):
  random_index_sym = random.randint(0, len(symbols) - 1)
  symbols_index.append(symbols[random_index_sym])
# print(symbols_index)

numbers_index = [] # this list will hold the numbers
for numberi in range(nr_numbers):
  random_index_num = random.randint(0, len(numbers) - 1)
  numbers_index.append(numbers[random_index_num])
# print(numbers_index)

combined_list = letters_index + symbols_index + numbers_index # this could be avoided since a list for all 3 for loops can be used.
#it can be done by appending values 
# print(combined_list)
random.shuffle(combined_list)
# print(combined_list)

passingword = ""
for item in combined_list:
  passingword += item

print(passingword)

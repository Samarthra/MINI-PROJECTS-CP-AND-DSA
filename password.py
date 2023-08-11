#importing string and random library
import string
import random

#input from the user
a = int(input("How many letters do you want in your password? "))
b = int(input("How many numbers do you want in your password? "))
c = int(input("How many symbols do you want in your password? "))

upper = string.ascii_uppercase
lower = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation

letter = random.choices(upper + lower,k=a)
num = random.choices(numbers, k=b)
sym = random.choices(symbols, k=c)


word = letter + num + sym
random.shuffle(word)

password = "".join(word)
print('The Generated Password is '+password)
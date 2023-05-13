#welcome to the Password Generator
import random

letters=list(range(ord("a"),ord("z")))
numbers= list(range(0,9))
symbols=["£","&","!","%","$"]

# print(chr(letters))

for number in range(ord("a"), ord("p")+1):
    print(chr(number))

print(numbers)

nr_letters=int(input("How many letters would like in your password?\n"))

nr_numbers=int(input("How many numbers would like in your password?\n"))

nr_symbols=int(input("How many symbols would like in your password?\n"))


# for i in range(9):
#     print(i)
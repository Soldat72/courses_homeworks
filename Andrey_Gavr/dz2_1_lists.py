# strings
import string
import random
letters = string.ascii_letters
numbers = string.digits
list1 = []
for i in range(10):
    length = random.randint(1, 10)
    list_letters = random.sample(letters, length)
    list_letters = "".join(list_letters)
    list1.append(list_letters)
print(list1)

list2 = []
for i in range(10):
    length = random.randint(1, 10)
    list_numbers = random.sample(numbers, length)
    list_numbers = "".join(list_numbers)
    list2.append(list_numbers)
print(list2)

dictionary = {}
for i in range(10):
    dictionary.update({list1[i]: list2[i]})
print(dictionary.keys())
print(dictionary.values()) 
print(dictionary.items())
print(dictionary)

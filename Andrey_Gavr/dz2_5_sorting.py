import random
from string import ascii_letters
list1 = []
for i in range(5):
    list1.append(random.randint(1, 7))
sorted_list1 = sorted(list1, reverse=True)
print("Отсортированный список", sorted_list1)
letters = ascii_letters
for i in range(len(sorted_list1)):
    print("Номер буквы:", sorted_list1[i])
    print(letters[sorted_list1[i]-1:random.randint(len(sorted_list1), len(letters)):])

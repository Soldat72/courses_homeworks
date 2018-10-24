import random
list1 = []
for i in range(random.randint(1, 10)):
    list1.append(random.randint(1, 100))
print(list1, len(list1))
k = 1
while k < len(list1):
    for i in range(len(list1)-k):
        if list1[i] > list1[i+1]:
            # print(i, list1[i],  list1[i+1])
            list1[i], list1[i + 1] = list1[i + 1], list1[i]
            # print(list1)
    k += 1
print(list1)

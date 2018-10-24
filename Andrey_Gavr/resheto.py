while True:
    try:
        user_number = int(input("Введи натуральное целое число больше 1 го "))
        if user_number <= 1:
            continue
        else:
            break
    except ValueError:
        continue
# print(user_number)

list1 = []
for i in range(user_number+1):
    list1.append(i)

list1[1] = 0
print(list1)
i = 2
while i < user_number+1:
    if list1[i] != 0:
        n = i * 2
        while n < user_number+1:
            list1[n] = 0
            n = n + i
    i += 1
print(list1)
list2 = []
for i in list1:
    if list1[i] != 0:
        list2.append(list1[i])
print(list2)


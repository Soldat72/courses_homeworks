number = int(input("Enter number:"))+1
sign = "*"
for i in range(number):
    print(sign*i)


for i in range(number):
    print('\x20'*(number - i), sign*i*2)
    # print('{:^20}'.format('step'))





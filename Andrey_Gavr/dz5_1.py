import os
import collections


def input_file():
    file_input = input('Input path to file:')
    if os.path.isfile(file_input):    # возвращает False or True
        return file_input
    else:
        print("No such file or path")
        return False


def attempts():
    for i in range(3):
        f = input_file()
        if f:
            return f
    print("There were 3 attempts")
    exit()


path = attempts()
with open(path, 'r') as text_in_file:
    file_content = text_in_file.read()
    #    a = {sym.strip(): 1 for sym in file_content}  # dict
    list1 = list(file_content)
    list2 = []
    for i in range(len(list1)):
        if list1[i] != ' ':
            list2.append(list1[i])
    print(list1)
    print(list2)
    most_often_letter = dict(collections.Counter(list2).most_common(1))
    print(most_often_letter)


    # i = collections.Counter()
    # for sym in file_content:
    #   i[sym] += 1
    # print(i)
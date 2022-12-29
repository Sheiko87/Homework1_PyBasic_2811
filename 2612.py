# 3
from random import randint

my_list_1 = [randint(0, 200) for i in range(20)]
my_list_2 = [randint(0, 200) for i in range(20)]
my_result = []
print(my_list_1)
print()
print(my_list_2)
print()
my_result = my_list_1[::2] + my_list_2[1: len(my_list_2): 2]
print(my_result)
print()

# 11

my_str = input('Введите строку: ')
my_list = list(my_str)
li = []
for index in range(len(my_list)):
    if my_list[index] not in my_list[index + 1::] and my_list[index] not in my_list[:index]:
        li.append(my_list[index])
print(li)
print()

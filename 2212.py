# 1
import random

li = [random.randint(1, 200) for i in range(20)]
print(li)  # чтобы убедиться в том, что выбирает правильные элементы
for element in li:
    if element > 100:
        print(element, end=' ')
print()

# 2
import random

my_list = [random.randint(1, 200) for i in range(20)]
print(my_list)
my_results = list()
for element in my_list:
    if element > 100:
        my_results.append(element)
print('Новый список: ', my_results)
print()

# 3
i = int(input('Введите колличество чисел в списке: '))
import random

my_list = [random.randint(1, 200) for n in range(i)]
print(my_list)
if len(my_list) < 2:
    my_list.append(0)
    print(my_list, end=' ')
else:
    element = my_list[-1] + my_list[-2]
    my_list.append(element)
    print(my_list, end=' ')
print()

# 4
import random

li = [random.randint(1, 200) for i in range(20)]
print(li, end=' ')
print()
index = int(input('Введите индекс числа: '))
li = li[:index - 1] + li[index:]
print(li, end=' ') # для проверки
print()
li.pop()
print(li, end=' ')

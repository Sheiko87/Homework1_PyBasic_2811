## 1

persons = [{'name': 'John', 'age': 15}, {'name': 'Volodimir', 'age': 42},
           {'name': 'Jack', 'age': 45}, {'name': 'Vasul', 'age': 27}, {'name': 'Katerina', 'age': 15},
           {'name': 'Vladuslav', 'age': 47}]
# a
name = []
age_min = persons[0]['age']
for i in persons:
    if i['age'] <= age_min:
        age_min = i['age']
        name.append(i['name'])
print(name, end='')
print()

# b
names = []
longest_name_length = 0
for i in persons:
    if len(i['name']) > longest_name_length:
        longest_name_length = len(i['name'])
    #print(longest_name_length, end=' ')

for i in persons:
    if len(i['name']) == longest_name_length:
        names.append(i['name'])
print(names)
print()

# c
sum = 0
for i in persons:
    age = int(i['age'])
    sum = sum + age
    middle_age = int(sum / len(persons))
print(middle_age)
print()

## 2

my_dict_1 = {i: i * i for i in range(10)}
print(my_dict_1)
my_dict_2 = {i: i for i in range(15) if i % 2 == 1}
print(my_dict_2)
# a
li = []
for i in my_dict_1:
    for j in my_dict_2:
        if i == j:
            li.append(i)
print(li)
print()

# b
li1 = []
for i in my_dict_1:
    if i not in my_dict_2:
        li1.append(i)
print(li1)
print()

# c
print(my_dict_1.items())
dictionary = {}
for key in my_dict_1:
    if key not in my_dict_2:
        dictionary.update({key: my_dict_1[key]})
print(dictionary)
print()

# d
dictionary = {}
for key in {*my_dict_1, *my_dict_2}:
    if key in my_dict_1 and key in my_dict_2:
        dictionary.update([(key, [my_dict_1[key], my_dict_2[key]])])
    elif key in my_dict_1:
        dictionary.update([(key, my_dict_1[key])])
    elif key in my_dict_2:
        dictionary.update([(key, my_dict_2[key])])
print(dictionary)
print()

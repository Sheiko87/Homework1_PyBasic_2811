## 1

persons = [{'name': 'John', 'age': 15}, {'name': 'Volodimir', 'age': 42},
           {'name': 'Jack', 'age': 45}, {'name': 'Vasul', 'age': 27}, {'name': 'Katerina', 'age': 15}]
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
the_longest_name = persons[0]['name']
for i in persons:
    #    print(len(i['name']), end=' ')
    if len(i['name']) >= len(the_longest_name):
        the_longest_name = i['name']
        # print(the_longest_name,end=' ')
        names.append(the_longest_name)
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
for key in my_dict_1:
    if key not in my_dict_2:
        dictionary.update({key: my_dict_1[key]})
for j in my_dict_2:
    if j not in my_dict_1:
        dictionary.update({j: my_dict_2[j]})
    elif j in my_dict_1:
        dictionary.update({j: [my_dict_1[j], my_dict_2[j]]})
print(dictionary)
print()

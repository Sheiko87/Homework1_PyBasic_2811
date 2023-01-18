# 1
def print_strings(strings):
    my_list = []
    for index in range(len(strings)):
        if index % 2 != 0:
            my_list.append(strings[index][::-1])
        else:
            my_list.append(strings[index])
    return my_list


# print(print_strings(['jft', 'nhyr', 'sfth', 'vgt', 'gfh']))


# 2
def print_list(string):
    my_list = list()
    for element in string:
        if element[0] == 'a':
            my_list.append(element)
    return my_list

#print(print_list(['fgkf', 'anncnb', 'jbvka', 'anf']))

# 3
def letter_a(words):
    my_list = []
    for element in words:
        if 'a' in element:
            my_list.append(element)
    return my_list


# print(letter_a(['ahdbn','hfdv','fhgga','gajja','hfvjk']))

# 4
def strings_type(string_list):
    my_list = []
    for element in string_list:
        if isinstance(element, str):
            my_list.append(element)
    return my_list


# print(strings_type(['cggf', 25, 78, 'cfgh']))

# 5
def one_time_symbol(my_str):
    my_list = []
    for i in my_str:
        if my_str.count(i) == 1:
            my_list.append(i)
    return my_list


# print(one_time_symbol('jgjfkfdsjgfha'))

# 6
def print_symbol(str1, str2):
    my_list = []
    for i in str1:
        if i in str2:
            my_list.append(i)
    return my_list


# print(print_symbol('jhfd', 'jhgfdar'))

# 7
def symbol_double_str(str1, str2):
    my_list = []
    for i in set(str1):
        if str1.count(i) == 1 and str2.count(i) == 1:
            my_list.append(i)
    return my_list

print(symbol_double_str('vdhjs','dhhmn'))

# 1

def print_strings(list):
    for index in range(len(list)):
        for element in list:
            if index % 2 != 0:
                new_element = element[::-1]
                list.append(new_element)
            else:
                list.append(element)
    print(list)
    print()
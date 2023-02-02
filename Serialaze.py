# 1
def remove_word(filename: str, words: list):
    with open(filename, "rt") as file:
        text = file.read()
        new_text = text
        for word in words:
            if word in text:
                new_text = new_text.replace(word, '*')
        return new_text


import json


def new_file(filename):
    with open(filename, "w") as file:
        json.dump(remove_word("London.txt", ['London', 'is']), file)


# new_file("TEST.json")
# 2
def calc_words(filename: str):
    statistic = [{'Filename': filename}]
    with open(filename, "rt") as file:
        text = file.read()
        text = text.lower()
        text = text.replace('\n', ' ')
        text = text.replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').replace(':', ' ')
        for word in set(text.split()):
            statistic.append({'Word': word, 'Count': text.count(word)})
        return (statistic)


# print(calc_words("London.txt"))

import json


def new_file(filename):
    with open(filename, "a") as file:
        json.dump(calc_words("London.txt"), file)


new_file("stat.json")

# 3
def calc_words(filename: str):
    # my_di = {}
    # words = []
    statistic = []
    with open(filename, "rt") as file:
        text = file.read()
        text = text.lower()
        text = text.replace('\n', ' ')
        text = text.replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').replace(':', ' ')
        for word in set(text.split()):
            statistic.append({'Word': word, 'Count': text.count(word)})
        statistic.append({'Filename': filename})
        # print(statistic)
        return (statistic)


# calc_words("London.txt")



import csv


def new_file_csv(filename: str):
    text = calc_words(filename)
    with open('stat.csv', "w", newline="") as file:
        #print(text)
        for i in text:
            #print(i,end='\n')
            columns = i.keys()
            #print(columns)
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            writer.writerows(text)


#new_file_csv("London.txt")

#не выводит Filename
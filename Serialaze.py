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
    my_di = {}
    words = []
    statistic = {'Filename': filename}
    with open(filename, "rt") as file:
        text = file.read()
        text = text.lower()
        text = text.replace('\n', ' ')
        text = text.replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').replace(':', ' ')
        for word in text.split():
            words.append(word)
            if word in words:
            my_di.update({word: text.count(word)})
            statistic.update({'Words': words, 'Count': my_di})
        print(statistic)

        #            my_di.update({word: text.count(word)})
        #    return my_di


calc_words("London.txt")

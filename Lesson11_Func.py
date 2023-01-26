# 1 - не могу понять почему воспринимает только 1 слово из всего списка
def remove_word(filename: str, words: list):
    with open(filename, "rt+") as file:
        text = file.read()
        for word in words:
            if word in text:
                new_text = text.replace(word, '*')
        file.writelines(new_text)


#remove_word("London.txt", ['London', 'is'])


# 2
def calc_words(filename: str):
    my_di = {}
    with open(filename, "rt") as file:
        text = file.read()
        text = text.lower()
        text = text.replace('\n', ' ')
        text = text.replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').replace(':', ' ')
        for word in text.split():
            my_di.update({word: text.count(word)})
    return my_di

# print(calc_words("London.txt"))

# 1
def remove_word(filename: str, words: list):
    with open(filename, "rt") as file:
        text = file.read()
        #print(text)
        new_text = text
        for word in words:
            if word in text:
                new_text = new_text.replace(word, '*')
        #print(new_text)
        return new_text


def write_txt_file(filename: str):
    write_text = remove_word(filename, ['London', 'is'])
    with open(filename, 'w') as file:

       # print(write_text)
        file.write(write_text)


# remove_word("London.txt", ['London', 'is'])
write_txt_file("London.txt")


# 2
def calc_words(filename: str):
    my_di = {}
    with open(filename, "rt") as file:
        text = file.read()
        text = text.lower()
        text = text.replace('\n', ' ')
        text = text.replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').replace(':', ' ')
        for word in set(text.split()):
            my_di.update({word: text.count(word)})
    return my_di

# calc_words("London.txt")

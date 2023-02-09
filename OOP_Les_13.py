import json
import csv


class Employee:
    firstname = 'Ivasik'
    lastname = 'Telesik'
    age = 13
    email = 'ivasik_telesik1732@izkurnanog.ua'
    skills = ['ходить', "говорить", "кодить"]
    people_lang = ['Україньська', "Англійська"]
    coding_lang = ['Python', "C++", "lisp"]

    def __init__(self, firstname: str, lastname: str, age: int):
        # email: str, skills: str,
        #        people_lang: str, coding_lang: str):

        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    #   self.email = email
    #   self.skills = skills
    #   self.people_lang = people_lang
    #   self.coding_lang = coding_lang

    def show_parametrs(self):
        print(f'Firstname:{self.firstname}\nLastname:{self.lastname}\nAge:{self.age}\n'
              f'Email:{self.email}\nSkills:{self.skills}\nLanguage:{self.people_lang}\nCoding:{self.coding_lang}')

    def data_write(self):
        """
        собирает данные в словарь
        :return:
        """
        data = {}
        data['firstname'] = self.firstname
        data['lastname'] = self.lastname
        data['age'] = self.age
        data['email'] = self.email
        data['skills'] = self.skills
        data['people_lang'] = self.people_lang
        data['coding_lang'] = self.coding_lang
        return data

    def new_file_json(self):
        data = {}
        data['firstname'] = self.firstname
        data['lastname'] = self.lastname
        data['age'] = self.age
        data['email'] = self.email
        data['skills'] = self.skills
        data['people_lang'] = self.people_lang
        data['coding_lang'] = self.coding_lang
        # print(data)

        with open(f'{self.lastname}.json', "w") as file:
            json.dump(data, file)

    def csv_file_write(self):
        data = {}
        data['firstname'] = self.firstname
        data['lastname'] = self.lastname
        data['age'] = self.age
        data['email'] = self.email
        data['skills'] = self.skills
        data['people_lang'] = self.people_lang
        data['coding_lang'] = self.coding_lang

        with open(f'{self.lastname}.csv', "w") as file:
            writer = csv.DictWriter(file, fieldnames=data.keys(), delimiter=';')
            writer.writeheader()
            writer.writerow(data)


obj = Employee('Ivasik', 'Telesik', 13)
# print(obj)
# obj.show_parametrs()
# print(obj.data_write())
#print(obj.new_file_json())
#obj.csv_file_write()



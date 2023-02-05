# 1, 2
divide_values = [2, 0, None, "1", True, False, [], {}]
values_to_devide = [10, "1", None, True, False, [], 0, {}]
# 1
try:
    result = []
    for i in values_to_devide:
        for j in divide_values:
            num = i / j
            result.append(num)
    print(result)

except ZeroDivisionError:
    print("Ділити на нуль не можна!")
#    raise Exception("Щось пішло не так")

except TypeError:
    print("Не можна комбінувати ці типи даних")
# 2
except Exception:
    print("Щось пішло не так")

else:
    print("Ділення пройшло успішно!")

# 3
list_of_integers = [0, 1, 2, 3, 4, 5]
user_index = int(input('Введіть індекс числа зі списку: '))

try:
    number = list_of_integers[user_index]
    print(number)

except ValueError:
    print("Потрібно ввести ціле число!")

except IndexError:
    print("Такого індексу не існує!")

# 4
person_data = {"name": "Bolt", "age": 23, "gender": "male", "born_date": "06.07.1990"}
user_key = input('Введіть ключ: ')

try:
    value = person_data[user_key]
    print(value)

except KeyError:
    print("Такого ключа не існує!!")

finally:
    print("Чекаю наступного ключа!")
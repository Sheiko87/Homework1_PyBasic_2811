n = int(input('Введите колличество учеников : '))
k = int(input('Введите колличество яблок : '))
in_arms = n // k
in_box = n % k
print(f'У школьников по {in_arms} яблок')
print(f'В корзине {in_box} яблок')

class_1 = int(input('Введите колличество учеников класса А : '))
class_2 = int(input('Введите колличество учеников класса Б : '))
class_3 = int(input('Введите колличество учеников класса В : '))
number_desks = int(class_1 / 2 + class_1 % 2) + int(class_2 / 2 + class_2 % 2) + int(class_3 / 2 + class_3 % 2)
print(f'Нужно {number_desks}  парт')

number = int(input('Введите трехзначное число: '))
units = int(number % 10)
tens = int(number // 10 % 10)
hundreds = int(number // 100)
all_number = units * 100 + tens * 10 + hundreds
print(all_number)

numbers = int(input('Введите колличество секунд : '))
hours = int(numbers // 3600)
seconds = int(numbers % 3600)
lost_min = int(numbers - hours * 3600)
minutes = int(lost_min // 60)
lost_sec = int(seconds % 60)
hour = str(hours).zfill(2)
minut = str(minutes).zfill(2)
sec = str(lost_sec).zfill(2)
print(f'На часах {hour} : {minut} : {sec}')

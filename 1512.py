num_1 = float(input('Введите первое число: '))
num_2 = float(input('Введите второе число: '))
operator = input('Введите оператор: ')
if operator == '+':
    result = num_1 + num_2
    print(f'Результат сложения равен: {result}')
    print()
elif operator == '-':
    result = num_1 - num_2
    print(f'Результат вычитания равен: {result}')
    print()
elif operator == '*':
    result = num_1 * num_2
    print(f'Результат умножения равен: {result}')
    print()
else:
    result = num_1 / num_2
    print(f'Результат деления равен: {result}')
    print()

# 2
num = int(input('Введите число: '))
i = 1
res = 1
for i in range(1, num + 1):
    res = i ** 2
    i = i + 1
    if res <= num:
        print(res, end=' ')
    else:
        break
print()

# 3
number = int(input('Введите число: '))
n = 0
for i in range(2, number):
    if number % i == 0:
        n = n + 1
if n <= 0:
    print('Это число простое')
    print()
else:
    print('Это число не является простым')
    print()



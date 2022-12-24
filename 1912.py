# 1
my_string = '0123456789'
unit = 0
num = 0
k = 0  # счетчик повторений цикла
n = 0
p = 0  # счетчик цифр
while k <= 10:
    for j in range(0, 10):
        num = int(str(my_string)[n])
        k = k + 1
        result = unit + num
        n = n + 1
        unit = unit + 1
        print(result, end=' ')
    print()

    # else:
    # unit=unit+1
    # p=1
    # for i in range(p, 10):
    # num = int(str(my_string)[n])
    # k = k + 1
    # result = unit + num
    # n = n + 1
    # print(result, end=' ')
    # if n < 11:
    #   p=p+1
    #  print(result, end=' ')
pass

# 2
high = int(input('Введите высоту фигуры: '))

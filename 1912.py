# 1
my_string = '0123456789'
for edinicu in my_string:
    for desatki in my_string:
        res = int(edinicu + desatki)
        print(res, end=' ')
    print()

# 2
# B

strings = int(input('Введите высоту фигуры: '))
for s in range(1, strings + 1):
    for space in range(strings * 2 - s * 2):
        print('-', end='')
    for star in range(s * 2 - 1):
        print('*', end=' ')
    print()

# A
#            *
#          *   *
#        *       *
#      *           *
#    *               *
#  *                   *
# * * * * * * * * * * * * *

strings = int(input('Введите высоту фигуры: '))
p = 3
for s in range(1, strings + 1):
    for space in range(strings * 2 - s * 2):
        print('-', end='')
    if 2<=s<=6:
        for star in range(2):
            print('*','-'*(p-1), end='')
        p=p+4
    else:
        for star in range(s * 2 - 1):
            print('*', end=' ')
    print()

# ромб
strings = int(input('Введите высоту фигуры: '))
for s in range(0,strings+1):
    for j in range(0,strings-s):
        print('-',end='')
    for j in range(0,s):
        print('*',end=' ')
    print()
if s==strings:
    for s in range(strings-1,0,-1):
        for j in range(0,strings-s):
            print('-',end='')
        for j in range(0,s):
            print('*',end=' ')
        print()
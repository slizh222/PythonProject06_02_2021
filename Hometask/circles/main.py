# Вывод программы прямоуголника с помощью звездочек.

rows = 5
cols = 22

for r in range(rows):
    for c in range(cols):
        print('*', end='')
    print()

size = 8

for r in range(size):
    for c in range(r+1):
        print('*',end='')
    print()



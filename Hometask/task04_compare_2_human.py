# 4. Даны имена 2х человек (тип string). Если имена равны,
# то вывести сообщение о том, что люди являются тезками.

def compare_2_human(name1,name2):
    if name1 == name2:
        print("Люди являются тезками")
    else:
        print("Эти имена разные")

name1 = str(input("Введите имя первого человека : "))
name2 = str(input("Введите имя второго человека : "))
print(compare_2_human(name1,name2))

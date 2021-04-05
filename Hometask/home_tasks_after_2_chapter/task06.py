# Напишите программу, которая попросит пользователя ввести величину
# покупки. Затем программа должна вычислить федеральный и региональный налог с продаж.
# Допустим, что федеральный налог с продаж составляет 5%, а региональный - 2.5%.
# Программа должна показать сумму покупки, федеральный налог с продаж, региональный
# налог с продаж, общий налог с продаж и общую сумму продажи (т. е. сумму покупки и
# общего налога с продаж).
# Подсказка: для представления 2.5% используйте значение 0.025, для представления
# 5% - 0.05.

x = int(input("Введите величину покупки : "))
fed_nalog = x*0.05
reg_nalog = x*0.025
sum_of_nalog = fed_nalog+reg_nalog
y = x+sum_of_nalog

print("Федеральный налог с продаж = ",fed_nalog)
print("Региональный налог с продаж = ",reg_nalog)
print("Общий налог с продаж = ",round(sum_of_nalog,2))
print("Общая сумма продажи = ",y)

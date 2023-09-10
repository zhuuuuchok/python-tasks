# Запрашиваем у пользователя ввод минимума диапазона
min = int(input('Please, enter the range minimum: '))
# Запрашиваем у пользователя максимума диапазона
max = int(input('Please, enter the range maximum: '))
# Запрашиваем у пользователя ввод шага
step = int(input('Please, enter the step: '))

# Создаем функцию и присваиваем параметры
def series_of_num(min,max,step):
    # С помощью цикла for и встроенной функции range
    # перебираем заданный диапазон чисел с указанным шагом
    for i in range(min,max+1,step):
        print(i)
# Вызываем функцию
series_of_num(min,max,step)
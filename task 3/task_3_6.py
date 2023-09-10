# Запрашиваем у пользователя ввод числа
number = int(input('Please, enter the number: '))

# Создаем функцию для рассчета факториала
def calculation_fact (number, factorial=1):

    # Вычислим факториал, если при каждом прохождении цикла while,
    # мы будем отнимать 1 от переменной number
    while number > 0:
        factorial = factorial * number
        number -= 1
    # Возвращаем результат вычисления факториала
    return factorial
print(f'This is a factorial of entered number: {calculation_fact(number)}')
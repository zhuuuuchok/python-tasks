# Запрашиваем у пользователя ввод проверяемого числа
num = int(input('Please, enter the number: '))

# Создаем функцию
def check(num):

    # С помощью побитовой операции & проверяем число на нечетность.
    # Если последний бит введенного числа будет = 1, то число нечетное
    if num & 1:
        print (f'Entered number is not even')

    # Если последний бит введенного числа = 0, то число четное
    else:
        print (f'Entered number is even')
        
# Вызываем функцию
check(num)
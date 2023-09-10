#  Запрашиваем ввод первого аргумента
n_1 = int(input('Please, enter the first number: '))

# Запрашиваем ввод второго аргумента
n_2 = int(input('Please, enter the second number: '))

# Запрашиваем ввод третьего аргумента. 
# Пользователю нужно выбрать одну из операций в скобках
choice = input('Please, enter the operation (+,-,*,/): ')

# Создаем переменные в которые помещаем лямбда-выражения
# После lambda  указаны параметры для выражения, 
# после ":" указывается операция для lambda-выражения
sum = lambda n_1, n_2: n_1 + n_2
minus = lambda n_1, n_2: n_1 - n_2
mult = lambda n_1, n_2: n_1 * n_2
division = lambda n_1, n_2: n_1 / n_2

# Символу, каждого математического действия,
# присваеваем одну из созданных ранее переменных

if choice == "+":
    print (f'Result of operation: {sum(n_1, n_2)}')
    
#   
elif choice == "-":
    print (f'Result of operation: {minus(n_1, n_2)}')
#    
elif choice == "*":
    print (f'Result of operation: {mult(n_1, n_2)}')
#    
elif choice == "/":
    print (f'Result of operation: {division(n_1, n_2)}')

# Если пользователь введет символ, который не используется в операциях,
# программа выведет следующее сообщение
else:
    print('select another option')    
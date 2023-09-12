def main():
    n_1 = int(input('Please, enter the first number: '))
    n_2 = int(input('Please, enter the second number: '))
    choice = input('Please, enter the operation ( + , - , * , / ): ')

    # Create variables in which we place lambda expressions
    # After lambda the parameters for the expression are specified, 
    # after ":" the operation for the lambda expression is indicated
    sum = lambda n_1, n_2: n_1 + n_2
    minus = lambda n_1, n_2: n_1 - n_2
    mult = lambda n_1, n_2: n_1 * n_2
    division = lambda n_1, n_2: n_1 / n_2

    # We assign the symbol of each mathematical operation to one of  variables
    if choice == "+":
        print (f'Result of operation: {sum(n_1, n_2)}')
    elif choice == "-":
        print (f'Result of operation: {minus(n_1, n_2)}')
    elif choice == "*":
        print (f'Result of operation: {mult(n_1, n_2)}')
    elif choice == "/":
        print (f'Result of operation: {division(n_1, n_2)}')
    else:
        print('select another option')
        
main()
def calculation_fact(number, factorial=1):
    while number > 0:
        factorial = factorial * number
        number -= 1
    return factorial


def main():
    number = int(input('Please, enter the number: '))
    print(f'This is a factorial of entered number: {calculation_fact(number)}')


main()

def main():
    year = int(input('Enter a year: '))

    def leap_year(year):
        if year % 4 != 0 :
            print('False')
        elif year % 100 == 0:
            if year % 400 == 0:
                print('True')
            else:
                print('False')
        else:
            print('True')

    print (f'{leap_year(year)}')

main()
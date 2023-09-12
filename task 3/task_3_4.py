def main():
    year = int(input('Enter a year: '))

    def leap_year(year):
        if year % 4 != 0 :
            return False
        elif year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True

    print (f'{leap_year(year)}')

main()
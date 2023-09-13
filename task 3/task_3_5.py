def season(num_of_month):
    if num_of_month == 12 or 1 <= num_of_month <= 2: 
        print('This is winter')
    elif 3 <= num_of_month <= 5:
        print('This is spring')
    elif 6 <= num_of_month <= 8:
        print('This is summer')
    elif 9 <= num_of_month <= 12:
        print('This is autumn')
    # if the user entered a non-existent month number, 
    # the following condition will work
    else:
        print('Try again')


def main():
    num_of_month = int(input('Please, enter number of the month: '))
    print(f'{season(num_of_month)}')
    

main()

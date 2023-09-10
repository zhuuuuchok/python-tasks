# ask the user to enter the month number
num_of_month = int(input('Please, enter number of the month: '))

# create a function
def season(num_of_month):

    # create a condition for checking
    # checking conditions for winter
    if num_of_month == 12 or 1<= num_of_month <= 2: 
        print('This is winter')

    # checking conditions for spring
    elif 3 <= num_of_month <= 5:
        print('This is spring')

    # checking conditions for summer
    elif 6 <= num_of_month <= 8:
        print('This is summer')

    # checking conditions for autumn
    elif 9 <= num_of_month <= 12:
        print('This is autumn')
        
    # if the user entered a non-existent month number, 
    # the following condition will work
    else:
        print('Try again')

print(f'{season(num_of_month)}')
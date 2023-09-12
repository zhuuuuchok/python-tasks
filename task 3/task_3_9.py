def main():
    num = int(input('Please, enter the number: '))
    
    def check(num):
        # Use "&" to check if a num is odd.
        # If the last bit of the entered num is = 1, then the num is odd
        if num & 1:
            print (f'Entered number is not even')
        else:
            print (f'Entered number is even')
    check(num)
    
main()
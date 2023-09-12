def main():
    min = int(input('Please, enter the range minimum: '))
    max = int(input('Please, enter the range maximum: '))
    step = int(input('Please, enter the step: '))

    def series_of_num(min,max,step):
        for i in range(min,max+1,step):
            print(i)

    series_of_num(min,max,step)
    
main()
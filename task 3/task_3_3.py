def main():
    n=int(input("Please, enter number of students: "))
    total_sum_of_marks = 0
    for i in range(n):
        name = input(f"Please,enter name of a student{i+1}: ")
        marks =int(input(f"Please,enter mark of a student {i+1}: "))
        total_sum_of_marks += marks
    #print(f'Name of student: {name},mark is {marks}')
    print(f'{total_sum_of_marks}')

   # for student in students:
   #     # Mark is stored in the 2nd element of the tuple(index=[1])
   #     total_sum_of_marks += student[1]
    
    average = int(total_sum_of_marks / n)
    print(f"Average mark of group is: {average}")

main()
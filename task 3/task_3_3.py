def main():
    n=int(input("Please, enter number of students: "))
    # Creating a list where all student data will be recorded
    students = []

    for i in range(n):
        name = input(f"Please,enter name of a student{i+1}: ")
        mark = int(input(f"Please,enter mark of a student {i+1}: "))
        # Write data to the tuple in the specified order
        students.append((name,mark))

    total_sum_of_marks = 0

    for student in students:
        # Mark is stored in the 2nd element of the tuple(index=[1])
        total_sum_of_marks += student[1]
    
    average = int(total_sum_of_marks / n)
    print(f"Average mark of group is: {average}")

main()
# Запрашиваем у пользователя ввод количества студентов
n=int(input("Please, enter number of students: "))

# создание списка, куда будут записываться все данные о студенте,
# которые ввел пользователь
students = []

# с помощью цикла for запрашиваем ввод данных о студенте n раз
for i in range(n):
    name = input(f"Please,enter name of a student{i+1}: ")
    mark = int(input(f"Please,enter mark of a student {i+1}: "))
    # записываем данные в кортеж в указаном порядке
    students.append((name,mark))
#print("Список студентов и их оценок: ") 
#for name,mark in students:
 #       print(f"{name}: {mark}")

# создаем новую переменную со значением 0
total_sum_of_marks = 0

# цикл перебирает все элементы списка students
for student in students:
    # каждый элемент списка является кортежем(содержащим имя и оценку).
    # оценка студента хранится во втором элементе кортежа индекс которого=[1]
    # присваиваем переменной результат сложения всех оценок 
    total_sum_of_marks += student[1]

# вычисление средней оценки   
average = int(total_sum_of_marks / n)
# вывод средней оценки
print(f"Average mark of group is: {average}")

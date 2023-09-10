import csv
import os
#проверка существования файла
file_path = "C:\\Users\\Юлия\\.vscode\\data.csv"
if os.access(file_path, os.F_OK) == True:
            print("Файл существует")

with open('C:\\Users\\Юлия\\.vscode\\data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile,delimiter=(','))
# next считывает первую строку файла,к-я является заголовочной
    head = next(reader)
#создается словарь data, для хранения данных
    data= {}

    for row in reader:
        #enumerate возвращает индекс и значение данных
        for i, value in enumerate(row):
            if i not in data:
                data[i] = []
            data[i].append(float(value))

for i, values in data.items():
    print(f"{head[i]}: min = {min(values)}, max = {max(values)}")
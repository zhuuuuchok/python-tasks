import re
import os
#проверка существования файла
file_path = "C:\\Users\\Юлия\\.vscode\\input.txt"
if os.access(file_path, os.F_OK) == True:
            print("Файл существует")

with open('C:\\Users\\Юлия\\.vscode\\input.txt' , 'r') as f:
    text = f.read()

sentences = re.split(r'[.!?]', text)
number_of_sentences=len(sentences)

#используем регулярное выражение, чтобы искать слова в тексте, не учитывая знаки препинания и перенос строки
words = re.findall(r'\b\w+\b', text)
number_of_words = len(words)

long_words = [word for word in words if len(word) > 5]
num_of_long_words = len(long_words)
print(sentences)

# создаем файлик для записи вывода
with open('output.txt', 'w') as f:
    f.write (f'Количество предложений в тексте: {number_of_sentences-1}\n')
    f.write (f'Количество слов в тексте: {number_of_words}\n')
    f.write (f'Количество слов в тексте, длиннее 5 символов: {num_of_long_words}\n')

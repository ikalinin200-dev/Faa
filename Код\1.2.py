new_name = input("Введите новое имя: ")

with open('Students.txt', 'a', encoding='utf-8') as file:
    file.write(new_name + '\n')

print("\nОбновлённое содержимое файла:")
with open('Students.txt', 'r', encoding='utf-8') as file:
    print(file.read())
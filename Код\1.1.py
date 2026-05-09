with open('Students.txt', 'w', encoding='utf-8') as file:
    file.write('Александр\n')
    file.write('Мария\n')
    file.write('Дмитрий\n')
    file.write('Елена\n')
    file.write('Иван\n')

print("\nСодержимое файла для проверки:")
with open('Students.txt', 'r', encoding='utf-8') as file:
    print(file.read())
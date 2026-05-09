print("Содержимое файла Students.txt:")
with open('Students.txt', 'r', encoding='utf-8') as file:
    students = [line.strip() for line in file if line.strip()]

for i, name in enumerate(students, 1):
    print(f"{i}. {name}")

chosen_name = input("\nВведите имя, которое нужно выбрать: ")

if chosen_name in students:
    with open('Chosen.txt', 'w', encoding='utf-8') as file:
        file.write(chosen_name)
    print(f"Имя '{chosen_name}' сохранено в файл Chosen.txt")

    students.remove(chosen_name)
    with open('Remaining.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(students))
    print(f"Остальные имена сохранены в файл Remaining.txt")
else:
    print(f"Имя '{chosen_name}' не найдено в файле.")

print("\nПроверка файлов:")
for filename in ['Chosen.txt', 'Remaining.txt']:
    print(f"\n{filename}:")
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
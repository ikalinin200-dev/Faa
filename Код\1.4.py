filename = input("Введите имя файла: ")
text = input("Введите текст для записи: ")

with open(filename, 'w', encoding='utf-8') as file:
    file.write(text.upper())

print(f"\nТекст записан в файл {filename} заглавными буквами.")

print("\nСодержимое файла для проверки:")
with open(filename, 'r', encoding='utf-8') as file:
    print(file.read())
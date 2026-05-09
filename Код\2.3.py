import csv

count = int(input("Сколько записей хотите добавить? "))

new_records = []
for i in range(count):
    print(f"\nЗапись {i + 1}:")
    book_name = input("Наименование книги: ")
    author = input("Писатель / Автор: ")
    country = input("Страна автора: ")
    year = input("Год издания: ")
    new_records.append([book_name, author, country, year])

with open('Books.csv', 'a', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(new_records)

print(f"\nДобавлено записей: {count}")
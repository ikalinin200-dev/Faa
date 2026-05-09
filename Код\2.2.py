import csv

book_name = input("Введите наименование книги: ")
author = input("Введите писателя/автора: ")
country = input("Введите страну автора: ")
year = input("Введите год издания: ")

with open('Books.csv', 'a', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([book_name, author, country, year])

print("\nСодержимое файла Books.csv:")
with open('Books.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        print(' | '.join(row))
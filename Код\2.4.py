import csv

def read_books():
    with open('Books.csv', 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file, delimiter=';')
        header = next(reader)
        books = list(reader)
    return header, books

def save_books(header, books):
    with open('Books.csv', 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(header)
        writer.writerows(books)

def show_numbered(header, books):
    print(f"{'№':<4} {' | '.join(header)}")
    print('-' * 80)
    for i, book in enumerate(books, 1):
        print(f"{i:<4} {' | '.join(book)}")

# Основная программа
header, books = read_books()

while True:
    print("\nМеню:")
    print("1 - Поиск книг по автору")
    print("2 - Поиск книг по году издания")
    print("3 - Вывод всех данных с нумерацией")
    print("4 - Изменение данных")
    print("5 - Выход")

    choice = input("\nВыберите действие: ")

    if choice == '1':
        author = input("Введите автора для поиска: ")
        found = False
        for book in books:
            if author.lower() in book[1].lower():
                print(' | '.join(book))
                found = True
        if not found:
            print(f"Книг автора '{author}' не найдено.")

    elif choice == '2':
        start_year = int(input("Введите начальный год: "))
        end_year = int(input("Введите конечный год: "))
        found = False
        for book in books:
            year = int(book[3])
            if start_year <= year <= end_year:
                print(' | '.join(book))
                found = True
        if not found:
            print(f"Книг за {start_year}-{end_year} годы не найдено.")

    elif choice == '3':
        show_numbered(header, books)

    elif choice == '4':
        show_numbered(header, books)
        action = input("\nЧто сделать? (удалить/изменить): ").lower()

        if action == 'удалить':
            num = int(input("Номер строки для удаления: "))
            if 1 <= num <= len(books):
                del books[num - 1]
                save_books(header, books)
                print("Строка удалена.")
            else:
                print("Неверный номер строки.")

        elif action == 'изменить':
            num = int(input("Номер строки для изменения: "))
            if 1 <= num <= len(books):
                print("Оставьте поле пустым, чтобы не менять.")
                new_name = input(f"Новое название ({books[num-1][0]}): ")
                new_author = input(f"Новый автор ({books[num-1][1]}): ")
                new_country = input(f"Новая страна ({books[num-1][2]}): ")
                new_year = input(f"Новый год ({books[num-1][3]}): ")

                if new_name:
                    books[num-1][0] = new_name
                if new_author:
                    books[num-1][1] = new_author
                if new_country:
                    books[num-1][2] = new_country
                if new_year:
                    books[num-1][3] = new_year

                save_books(header, books)
                print("Данные изменены.")
            else:
                print("Неверный номер строки.")

    elif choice == '5':
        print("Выход из программы.")
        break

    else:
        print("Неверный выбор.")
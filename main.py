def show_message(message):
    print(message)


def show_collection(collection):
    if len(collection) == 0:
        print("Список заметок пуст.")
    else:
        print("\nМои заметки:")
        for i, note in enumerate(collection, 1):
            print(f"{i}. {note}")


notes = []

while True:
    print("\n--- TASK MANAGER ---")
    print("1 - Показать заметки")
    print("2 - Добавить заметку")
    print("3 - Изменить заметку")
    print("4 - Удалить заметку")
    print("5 - Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        show_collection(notes)

    elif choice == "2":
        note = input("Введите заметку: ")

        if note:
            notes.append(note)
            show_message("Заметка добавлена!")
        else:
            show_message("Нельзя добавить пустую заметку.")

    elif choice == "3":
        show_collection(notes)

        if notes:
            number = int(input("Введите номер заметки: "))
            new_note = input("Введите новый текст: ")

            if 1 <= number <= len(notes):
                notes[number - 1] = new_note
                show_message("Заметка изменена!")
            else:
                show_message("Такой заметки нет.")

    elif choice == "4":
        show_collection(notes)

        if notes:
            number = int(input("Введите номер заметки: "))

            if 1 <= number <= len(notes):
                notes.pop(number - 1)
                show_message("Заметка удалена!")
            else:
                show_message("Такой заметки нет.")

    elif choice == "5":
        show_message("Программа завершена.")
        break

    else:
        show_message("Неверный выбор.")
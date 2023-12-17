import json
import os
from datetime import datetime

from note_controller import NoteController


def main():
    controller = NoteController()

    while True:
        print("\n Легенда:")
        print("1. Просмотреть заметки")
        print("2. Добавить новую заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            controller.display_notes()
        elif choice == '2':
            controller.add_note()
        elif choice == '3':
            controller.edit_note()
        elif choice == '4':
            controller.delete_note()
        elif choice == '5':
            print("Выход из программы заметок.")
            break
        else:
            print("Неверное действие. Выберите существующий вариант 1-5.")


if __name__ == "__main__":
    main()

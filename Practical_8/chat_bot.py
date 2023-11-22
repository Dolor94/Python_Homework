import json
import os

telephone_numbers = {}

def clear(): return os.system("cls")
clear()

def save():
    with open("Guide.json", "w", encoding="utf-8") as gd:
        gd.write(json.dumps(telephone_numbers, ensure_ascii=False, indent=0))
    print("Справочник был успешно сохранен в файле Guide.json")

def load():
    global telephone_numbers
    with open("Guide.json", "r", encoding="utf-8") as gd:
        telephone_numbers=json.load(gd)
    print("Справочник был успешно загружен из файла Guide.json")

print("Добро пожаловать в телефонный справочник!\nДля просмотра перечня команд, напишите /help")
flag = True
while flag:
    command = input("Введите команду: ")
    if command.lower() == "/add":
        name = input("Введите имя: ").title()
        number = input("Введите номер: ")
        telephone_numbers[name] = number
        print(f"Aбонент {name} успешно добавлен в справочник!")
    elif command.lower() == "/del":
        del_name = input("Введите Имя которое нужно удалить: ").title()
        if del_name in telephone_numbers:
            del telephone_numbers[del_name]
            print(f"Aбонент {del_name} успешно удалён из справочника!")
        else:
            print(f"Aбонент {del_name} в справочнике не найден!")
    elif command.lower() == "/all":
        for key, value in telephone_numbers.items():
            print(key,':', value)
    elif command.lower() == "/help":
        print("""/add - добавление номера
/del - удаление номера
/edit - редактирование номера
/all - показать все номера
/stop - завершение работы бота
/help - показать команды
/load - загрузка данных из файла
/save - cохранение данных в файл
""")
    elif command.lower() == "/edit":
        edit_abonent = input("Введите Имя абонента для его редактирования: ").title()
        if edit_abonent in telephone_numbers:
            telephone_numbers[edit_abonent] = input("Введите новый номер абонента: ")
            print(f"Номер абонента {edit_abonent} успешно изменён!")
        else:
            print(f"Aбонент {edit_abonent} в справочнике не найден!")
    elif command.lower() == "/save":
        save()
    elif command.lower() == "/load":
        load()
    elif command.lower() == "/stop":
        print("Справочник закончил работу. До свидания!")
        flag = False
    else:
        print("Данной команды не существует!\nДля ознакомления со списком команд напишите: /help")


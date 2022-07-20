documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

def people(documents):
    numb = input('Введите номер документа: ')
    for document in documents:
        if numb == document['number']:
            print(document['name'])
        else:
            print('Такого документа нет')
    print(documents)

def shelf(directories):
    numb = input('Введите номер документа: ')
    for key, direct in directories.items():
        for dir_ in direct:
            if numb == dir_:
                print(key)
            else:
                print("Такого номера нет")
    print(directories)

def list_(documents):
    for row in documents:
        print(row['type'] ,end='')
        for value in list(row.values())[1:]:
            print(f' "{value}"',end="")
        print(';')


def add(documents, directories):
    my_dict = {"type": [], "number": [], "name": []}
    my_dict["type"] = input("Введите тип документа: ")
    my_dict["number"] = input("Введите номер документа: ")
    my_dict["name"] = input("Введите номер: ")
    documents.append(my_dict)
    shelf = input("Введите номер полки: ")
    for key, value in directories.items():
        if key != shelf:
            continue
        value.append(my_dict["number"])

    print(directories)
    print(documents)

def delete(documents, directories):
    numb = input("Введите номер документа: ")
    for document in documents:
        if numb == document['number']:
            documents.pop()
        else:
            print('Такого номера нет')
    print(documents)



cmd = input('Введите Вашу комманду: ')
if cmd == 'l': list_(documents)
elif cmd == 'p': people(documents)
elif cmd == 's': shelf(directories)
elif cmd == 'a': add(documents, directories)
elif cmd == 'd': delete(documents, directories)
else: print('Такой комманды нет')




# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. Предусмотрите сценарий, когда пользователь
# вводит несуществующий документ;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. Корректно обработайте кейсы,
# когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку;
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. Предусмотрите случай,
# когда пользователь добавляет полку, которая уже существует.;
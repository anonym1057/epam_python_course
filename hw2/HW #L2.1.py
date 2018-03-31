phonebook = {}


def add_name_phone(name, phone):
    """add name with phone in dict phonebook

    :param name: name of person.
    :type name: str.
    :param phone: phone of the person.
    :type phone: int.
    :returns: none.
    """

    if name in phonebook:
        if phone not in phonebook[name]:
            phonebook[name] += [phone]
            print(f"В справочнике присутствует {name}. Добавлен телефон {phone}.")
        else:
            print("В справочнике уже присутвует такое имя c телефоном.")
    else:
        phonebook[name] = [phone]
        print(f"Добавлен новое имя {name} c  телефоном {phone}.")


def print_phone(name):
    """print name of the person and all phones in dict phonebook

    :param name: name of person.
    :type name: str.
    :returns: none.
    """
    if name in phonebook:
        print("номер", "телефон", sep='\t')
        for phone in phonebook[name]:
            print(name, phone, sep='\t')
    else:
        print(f"Имя {name} отсутствует в справочнике")


def delete_name(name):
    """delete name with all phones in dict phonebook

    :param name: name of person.
    :type name: str.
    :returns: none.
    """
    if name in phonebook:
        phonebook.pop(name)
        print("Имя удалено")
    else:
        print(f"Имя {name} отсутствует в справочнике")

k=1
while(k!=0):
    if k==0:
        break;
    elif k==1:
        print("0 - Выход",
             "1 - Вывести действия",
             "2 - Добавить имя человека и телефон",
             "3 - Вывести телефон человека",
             "4 - Удалить имя человека",sep='\n')
    elif k==2:
        name=input("Имя: ")
        phone=int(input("Телефон: "))
        add_name_phone(name,phone)
        pass
    elif k==3:
        name=input("Имя: ")
        print_phone(name)
        pass
    elif k==4:
        name=input("Имя: ")
        delete_name(name)
        pass
    else:
        print("Не верный номер действия!")
    k=int(input("Действие: "))


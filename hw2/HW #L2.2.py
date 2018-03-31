def select(*field_name):
    """ Takes a list of fields that must be in the resulting list

    :param field_name: fields
    :type field_name:: tuple.
    :returns: tuple.
    """
    return field_name


def field_filter(field_name, collection):
    """Takes the name by which it is necessary to filter and the iterable object
    - the values that should be in the resulting list

    :param field_name: name by which it is necessary
    :type field_name: str
    :param collection: iterable object
    :type collection: tuple.
    :returns: list
    """
    return [field_name, list(collection)]


def query(collection, select, *field_filter):
    """ Selects the required fields and filters them.

    :param collection: data
    :type collection: list
    :param select: fields that must be in the resulting list
    :type select: tuple
    :param *field_filter: filter the data
    :type *field_filter: tuple.
    :returns: list
    """
    list_new = []
    for data_dict in collection:
        if filter_dict(data_dict, field_filter):
            list_new += [select_dict(data_dict, select)]
    return list_new


def filter_dict(dict_data, field_filter):
    """Determines whether the data dict passes through all filters

    :param dict_data: data dictionary
    :type dict_data: dict
    :param field_filter: filter the data
    :type field_filter: tuple.
    :returns: bool
    """
    check = True
    for filters in field_filter:
        key = filters[0]
        for itt_data in filters[1]:
            if dict_data[key] == itt_data:
                break
        else:
            # если значения из списка не попалось
            check = False
    return check


def select_dict(dict_old, select):
    """ selects the required fields from all and forms a new dictionary

    :param dict_old: data dict
    :type dict_old: dict
    :param select: field select
    :type select: tuple.
    :returns: dict
    """
    # выбираем нужные данные для возврата
    dict_new = {}
    for key in select:
        #записываем их в словарь
        dict_new[key] = dict_old[key]
    return dict_new



friends = [
    {'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол', 'email': 'email@email.com'},
    {'name': 'Эмили', 'gender': 'Женский', 'sport': 'Волейбол', 'email': 'email1@email1.com'},
]
print(query(
    friends,
    select('name', 'gender', 'sport'),
    field_filter('sport', ['Баскетбол', 'Волейбол']),
    field_filter('gender', ['Мужской']),
))
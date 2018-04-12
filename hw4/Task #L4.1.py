def get_course(data):
    """
    Returns the courses present in the data
    :param data: list of dict
    :return: set of course
    """
    return {item['course'] for item in data}


def get_data_for_course(data, course):
    """
    Returns data sorted filtered by field 'course'
    :param data: list of dict
    :param course: str
    :return: list of dict
    """
    return sorted([item for item in data if item['course'] == course], key=lambda x: x['rate'], reverse=True)


def print_top_course(data, course, top_n=3):
    """
    Print top_n students for 'course'
    :param data:list of dict
    :param course: str
    :param top_n: int
    :return: none
    """
    print('\n',course)
    [print("\t",stage, item['name'], item['rate']) for item, stage in
     zip(get_data_for_course(data, course), range(1, top_n + 1))]


def print_top_all_courses(data, top_n=3):
    """
    Print top_n students for all 'course'
    :param data: list of dict
    :param top_n: int
    :return: none
    """
    [print_top_course(data, course) for course in get_course(data)]


if __name__=='__main__':
    data = [{'name': 'Alexey', 'rate': 6, 'course': 'Python'},
            {'name': 'Kate', 'rate': 5, 'course': 'Python'},
            {'name': 'Tom', 'rate': 7, 'course': 'Java'},
            {'name': 'Bob', 'rate': 4, 'course': 'Java'},
            {'name': 'Liza', 'rate': 8, 'course': 'Python'},
            {'name': 'Mary', 'rate': 3, 'course': 'Python'},
            {'name': 'Max', 'rate': 9, 'course': 'JavaScript'},
            {'name': 'Kolya', 'rate': 2, 'course': 'Python'},
            {'name': 'Sasha', 'rate': 10, 'course': 'JavaScript'},
            {'name': 'Masha', 'rate': 1, 'course': 'Python'}]

    print_top_all_courses(data)
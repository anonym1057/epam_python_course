class SchoolMember:
    """ Class of any person at school

    """

    def __init__(self, name, years):
        self.name = name
        self.years = years
        print(f"Создан SchoolMember: {self.name}")

    def show(self):
        print(f"Имя: \"{self.name}\" Возраст:\"{self.years}\"")

    pass


class Teacher(SchoolMember):
    """ Class teacher

    """

    def __init__(self, name, years, salary):
        super().__init__(name, years)
        self.salary = salary
        print(f"Создан Teacher: {self.name}")

    def show(self):
        print(f"Имя: \"{self.name}\" Возраст:\"{self.years}\" Зарплата:\"{self.salary}\"")

    pass


class Student(SchoolMember):
    """ Class student
    """

    def __init__(self, name, years, mark_sum):
        super().__init__(name, years)
        self.mark_sum = mark_sum
        print(f"Создан Students: {self.name}")

    def show(self):
        print(f"Имя: \"{self.name}\" Возраст:\"{self.years}\" Оценки:\"{self.mark_sum}\"")

    pass


if __name__ == '__main__':
    persons = [Teacher("Mr.Poopybutthole", 40, 3000), Student("Morty", 16, 75)]
    for person in persons:
        person.show()

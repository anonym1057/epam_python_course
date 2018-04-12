import abc
import functools
import decimal as dc

dc.Context(prec=10, rounding=dc.ROUND_HALF_UP)


class CurrencyDescr:
    """

    """
    def __init__(self, label):
        self.label = label


    def __get__(self, instance, owner):
        return (instance.__dict__[self.label] / instance.course).quantize(dc.Decimal('.01'))


    def __set__(self, instance, value):
        if (value < 0):
            raise ValueError("Invalid!")
        else:
            instance.__dict__[self.label] = dc.Decimal(value * instance.course)


class course_dec(dc.Decimal):
    """

    """
    def __call__(self, cls):
        return dc.Decimal(self / cls.course).quantize(dc.Decimal('.01'))


    def __repr__(self):
        return str(self.quantize(dc.Decimal('.01')))

    def __str__(self):
        return str(self.quantize(dc.Decimal('.01')))


class CourseDescr:
    def __init__(self):
        self.value = course_dec(0)


    def __get__(self, instance, owner):
        return self.value


    def __set__(self, instance, value):
        if (value < 0):
            raise ValueError("Invalid, value < 0!")
        else:
            self.value = course_dec(value)


@functools.total_ordering
class Currency:
    """

    """
    value = CurrencyDescr('value')

    def __init__(self, value):
        self.value = value


    def __repr__(self):
        return str(self.value) + self.get_sign()


    def __str__(self):
        return str(self.value) + self.get_sign()


    @abc.abstractmethod
    def get_sign(self):
        """

        :return:
        """
        pass


    def to(self, cls):
        """

        :param cls:
        :return:
        """
        if issubclass(cls, Currency):
            curr = cls(0)
            curr.__dict__['value'] = Currency.get_real_value(self)
            return curr
        else:
            raise TypeError(f"Invalid type {type(other)}")


    @staticmethod
    def get_real_value(instance):
        """

        :param instance:
        :return:
        """
        return instance.__dict__['value']


    def __add__(self, other):
        if isinstance(other, Currency):
            sum_res = Currency.get_real_value(self) + Currency.get_real_value(other)
            res = Dollar(sum_res)
            return res.to(self.__class__)
        else:
            raise TypeError(f"Invalid type {type(other)}")


    def __radd__(self, other):
        if type(other) == (int) and other == 0:
            return self.to(self.__class__)
        else:
            raise TypeError(f"Invalid type {type(other)}.")


    def __sub__(self, other):
        if isinstance(other, Currency):
            sum_res = Currency.get_real_value(self) - Currency.get_real_value(other)
            res = Dollar(sum_res)
            return res.to(self.__class__)
        else:
            raise TypeError(f"Invalid type {type(other)}")


    @functools.total_ordering
    def __eq__(self, other):
        if isinstance(other, Currency):
            return Currency.get_real_value(self) == Currency.get_real_value(other)
        else:
            raise TypeError(f"Invalid type {type(other)}")


    def __lt__(self, other):
        if isinstance(other, Currency):
            return Currency.get_real_value(self) < Currency.get_real_value(other)
        else:
            raise TypeError(f"Invalid type {type(other)}")


class Dollar(Currency):
    """

    """
    default_init=False
    course = CourseDescr()

    def __init__(self, value):
        if not self.default_init:
            self.course = 1
            self.default_init = True
        self.value = value


    def get_sign(self):
        return " $"


class Euro(Currency):
    """

    """
    course = CourseDescr()
    default_init = False

    def __init__(self, value):
        if not self.default_init:
            self.course = 1.2
            self.default_init = True
        self.value = value


    def get_sign(self):
        return " €"


class Ruble(Currency):
    """

    """
    course = CourseDescr()
    default_init = False

    def __init__(self, value):
        if not self.default_init:
            self.course = 0.02
            self.default_init = True
        self.value = value

    def get_sign(self):
        return " ₽"


if __name__=='__main__':
    d = Dollar(5000)
    e = Euro(5)
    r = Ruble(1000)

    print("d: Dollar:", d)
    print("d.course (к долару)",d.course)
    print("e: Euro:", e)
    print("e.course (к долару)", e.course)
    print("r: Ruble:", r)
    print("r.course (к долару)", r.course)

    print("e.to(Dollar): ", e.to(Dollar))
    print("sum([Euro(i) for i in range(5)]): ",sum([Euro(i) for i in range(5)]))
    print("e > Euro(6): ",e > Euro(6) )
    print("e + Dollar(10)" , e + Dollar(10))
    print("Dollar(10) + e",Dollar(10) + e )
    print("e.course = 2")
    e.course = 2
    print("e: ",e)
    print("Euro.course(Dollar): ", Euro.course(Dollar))
    print("Euro.course(Ruble): ",Euro.course(Ruble))


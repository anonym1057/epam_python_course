class ClassPropertyDescr():
    """
    Class decriptor for function
    fget is a function to be used for getting an attribute value, and likewise
    """

    def __init__(self, fget, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, instance, owner):
        return self.fget.__get__(instance, owner)()

    def __set__(self, obj, value):
        return self.fset.__get__(obj, type(obj))(value)

    def setter(self, func):
        self.fset = func
        return self


def prop(func):
    """
    Decorator. func is a function of a class that becomes an attribute
    :param func: func of class
    :return: descroptor of func
    """
    return ClassPropertyDescr(func)


class Something:
    """
    Class doing something
    """

    def __init__(self, x):
        self.x = x

    @prop
    def attr(self):
        """
        Return square of a x
        :return: square of a x
        """
        return self.x ** 2

    @attr.setter
    def attr_setter(self, update):
        self.x = update
        return


if __name__ == '__main__':
    s = Something(10)
    print(s.attr)
    s.attr=3
    print(s.attr)

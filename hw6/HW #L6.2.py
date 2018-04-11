class ClassPropertyDescr():
    """
    Class decriptor for function
    fget is a function to be used for getting an attribute value, and likewise
    """

    def __init__(self, fget):
        self.fget = fget

    def __get__(self, instance, owner):
        return self.fget.__get__(instance, owner)()


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
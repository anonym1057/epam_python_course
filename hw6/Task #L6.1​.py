class Price:
    """
    Descriptor of price
    """
    def __init__(self, label):
        self.label = label

    def __get__(self, instance, owner):
        print("get")
        if self.label in instance.__dict__:
            return instance.__dict__[self.label]
        else:
            print(f"{self.label} delete")

    def __set__(self, instance, value):
        if (value < 0 or value > 100):
            raise ValueError("The price should be from 0 to 100")
        else:
            print("set")
            instance.__dict__[self.label] = value

    def __delete__(self, instance):
        print("del")
        del instance.__dict__[self.label]
        pass


class Book:
    """
    Class of book
    """
    price = Price("price")

    def __init__(self, author, name_book, pr):
        self.author = author
        self.name_book = name_book
        self.price = pr


if __name__ == '__main__':
    b = Book("aa", "b", 14)
    a = Book("bb", "c", 100)
    print("b.price: ", b.price)
    print("a.price: ", a.price)
    b.price = 12
    print("b.price=12")
    print("b.price: ", b.price)
    print("a.price: ", a.price)
    del b.price
    print("del b.price")
    print("b.price: ", b.price)
    pass

import functools


# фабрика с аргументами
def fabric(f_lam):
    """
    Фабрика декораторов(также декоратор).
    Фабрика (функция) принимает аргумент - функцию(lambda) и декоратор.
    Возвращает декоратор, который должен вызывать функцию(lambda)
    с аргументом - результатом декорируемого декоратора.
    Присутствует атрибут для включения и выключения декорируемого декоратора. Функция(lambda) при этом будет отрабатывать.
    Атрибут выключается все декорируемые декораторы.
    Декорируемы декоратор  всегда используется со скобками (@deco())


    :param f_lam: function(lambda) with one argument
    :type f_lam:: function
    :returns: function - decorator.
    """

    # фабрика
    def fabric_args(deco):
        @functools.wraps(deco)
        # внутрення функция фабрики
        def wrapper(*dargs, **dkwargs):
            # сам декоратор
            def decorator(func):
                @functools.wraps(func)
                # внутренная функция декоратора
                def inner(*args, **kwargs):
                    if fabric.state_all:
                        result_func = deco(func, *dargs, **dkwargs)
                    else:
                        result_func = func
                    return f_lam(result_func(*args, **kwargs))

                return inner

            return decorator

        # если атрибут не объявлен
        if not hasattr(fabric, "state_all"):
            fabric.state_all = True

        def off():
            fabric.state_all = False
            pass

        def on():
            fabric.state_all = True
            pass

        fabric.on = on
        fabric.off = off

        return wrapper

    return fabric_args


@fabric(lambda x: x + 10)
def repeat(func, times=5):
    """ повторить вызов times раз, и вернуть среднее значение """

    @functools.wraps(func)
    def decorated(*args, **kwargs):
        times = 5
        total = 0
        for i in range(times):
            total += func(*args, **kwargs)
        return total / times

    return decorated


@repeat(5)
def foo_called():
    """Функция которая работает... и все"""
    print("Foo called!")
    return 2


@repeat()
def foo_called_1():
    """Функция которая работает... и все"""
    print("Foo called_1!")
    return 2


if __name__ == '__main__':
    print("Декоратор включен (по умолчанию)")
    print(foo_called())
    print("-----")
    print(foo_called_1())

    fabric.off()
    print("Декоратор выключен")
    print(foo_called())
    print("-----")
    print(foo_called_1())

    fabric.on()
    print("Декоратор включен")
    print(foo_called())
    print("-----")
    print(foo_called_1())

    print("Документация")
    help(repeat)
    help(foo_called)

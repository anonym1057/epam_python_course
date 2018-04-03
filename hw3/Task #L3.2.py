import time
import functools


def count_time(func):
    """ The decorator counts the time of the program """

    @functools.wraps(func)
    def inner(*args, **kwargs):
        time_beg = time.time()
        res = func(*args, **kwargs)
        time_end = time.time()
        print("Time:", time_end - time_beg)
        return res

    return inner


@count_time
def foo(x):
    for i in range(10000):
        for j in range(10000):
            pass
    return x


if __name__ == '__main__':
    print(foo(2))

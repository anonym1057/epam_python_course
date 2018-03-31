import time
import functools


def count_time(func):
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
    return x ** 2


print(foo(5))

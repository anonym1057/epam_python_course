import functools


def with_arguments(deco):
    """" The decorator let decorators use with arguments """
    @functools.wraps(deco)
    def wrapper(*dargs, **dkwargs):
        def decorator(func):
            result = deco(func, *dargs, **dkwargs)
            functools.update_wrapper(result, func)
            return result

        return decorator

    return wrapper


@with_arguments
def validate(func, low_bound, upper_bound):
    """The decorator check fo valid values of the arguments of the function
     If values don't valid, function doesn't start"""
    def inner(*args, **kwargs):
        check = True;
        tup = args[0]

        for j in tup:
            if j >= low_bound and j <= upper_bound:
                continue
            else:
                check = False
                break;

        if check:
            return func(*args, **kwargs)
        else:
            print("Function call is not valid!")
            return

    return inner


@validate(low_bound=0, upper_bound=256)
def set_pixel(pixel_values):
    print("Pixel created")

if __name__ == '__main__':
    print("(0,127,200): ")
    set_pixel((0, 127, 200))
    print("(0,127,300): ")
    set_pixel((0, 127, 300))


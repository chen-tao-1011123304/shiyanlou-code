from time import ctime, sleep


def timefun(func):
    def wrapped_func(*args, **kwargs):
        print('{0} called at {1}'.format(func.__name__, ctime()))
        func(*args, **kwargs)

    return wrapped_func


@timefun
def foo(a, b, c):
    print(a+b+c)


foo(3, 5, 6)
sleep(2)
foo(5, 6, 7)























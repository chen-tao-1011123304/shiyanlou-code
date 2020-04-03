from time import ctime, sleep


def timefun(func):
    def wrapped_func():
        print('{0}{1}'.format(func.__name__, ctime()))
        return func()

    return wrapped_func


@timefun
def foo():
    # return不显示
    return 'hahaha'


@timefun
def goInfo():
    print('i am go info')


foo()
sleep(2)
goInfo()
"""
fooWed Apr  1 22:20:41 2020
goInfoWed Apr  1 22:20:43 2020
i am go info
"""
print(foo())
"""
goInfoWed Apr  1 22:21:03 2020
i am go info
None
"""


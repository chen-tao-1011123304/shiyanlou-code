from time import ctime, sleep


def timefun(func):
    def wrapped_func():
        print('{0} called at {1}'.format(func.__name__, ctime()))
        func()

    return wrapped_func


# timefun(foo)  return wrapped_func()  pri...  func()
@timefun
def foo():
    print('i am foo')


foo()
sleep(2)
foo()











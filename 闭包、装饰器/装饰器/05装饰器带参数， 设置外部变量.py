from time import ctime, sleep


def timefun_arg(pre='hello'):
    def timefun(func):
        def wrapped_func():
            print('{0}{1}'.format(func.__name__, ctime()))
            print(pre)
            return func()

        return wrapped_func
    return timefun


@timefun_arg(pre='nihao')
def foo():
    print('i am foo')


@timefun_arg(pre='python')
def too():
    print('i am too')


foo()
sleep(2)
foo()

too()
sleep(2)
too()





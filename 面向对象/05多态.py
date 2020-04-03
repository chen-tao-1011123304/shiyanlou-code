class Dog(object):
    """这是一个狗类"""

    def __init__(self, name):
        self.name = name

    def game(self):
        print('{0}蹦蹦跳跳玩耍'.format(self.name))


class XiaoTianDog(Dog):
    """继承狗类"""

    def game(self):
        print('{0}飞到天上去玩耍'.format(self.name))


class Person(object):
    """这是一个人类"""

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print('{0}和{1}快乐玩耍'.format(self.name, dog.name))

        dog.game()


# 创建一个狗对象
wangcai = Dog('旺财')
wangcai.game()

xiaotian = XiaoTianDog('哮天犬')
xiaotian.game()

xm = Person('小明')
xm.game_with_dog(wangcai)
xm.game_with_dog(xiaotian)








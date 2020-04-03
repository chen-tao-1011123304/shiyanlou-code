class Cat:
    """这是一个猫类"""

    # 初始化
    def __init__(self, name):
        self.name = name
        print('{0}来了'.format(self.name))

    # 函数
    def eat(self):
        print('{0}吃'.format(self.name))

    # 对象名称
    def __str__(self):
        return '{0}对象'.format(self.name)

    # 结束前执行函数
    def __del__(self):
        print('{0}走了'.format(self.name))


tom = Cat('tom')
tom.eat()
print(tom)






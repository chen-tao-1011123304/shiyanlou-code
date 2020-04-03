"""
小明 体重 75.0 公斤
小明每次 跑步 会减肥 0.5 公斤
小明每次 吃东西 体重增加 1 公斤
"""


class Person:
    """这是一个人类"""

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        print("会减肥 0.5 公斤")
        self.weight -= 0.5
        print('{0}'.format(self.weight))

    def eat(self):
        print("体重增加 1 公斤")
        self.weight += 1
        print("{0}".format(self.weight))

    def __str__(self):
        return "目前姓名{0}体重{1}".format(self.name, self.weight)


xm = Person('小明', 75)
xm.run()
xm.eat()
xm.name = '大明'
print(xm.name)
print(xm)



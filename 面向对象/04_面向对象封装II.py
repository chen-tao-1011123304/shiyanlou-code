"""
士兵 许三多 有一把 AK47
士兵 可以 开火
枪 能够 发射 子弹
枪 装填 装填子弹 —— 增加子弹数量
"""


class Gun:
    """这是一个枪类"""

    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count
        print('添加子弹{0}'.format(self.bullet_count))

    def shoot(self):
        if self.bullet_count <= 0:
            print('没有子弹')
        else:
            self.bullet_count -= 1
            print('射击')
            print('枪类型{0}， 子弹数量{1}'.format(self.model, self.bullet_count))


class Solider:
    """这是一个士兵类"""

    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None:
            print('{0}还没枪'.format(self.name))

            return

        self.gun.add_bullet(30)
        self.gun.shoot()


# 创建枪对象
ak = Gun(model='ak47')
ak.add_bullet(30)
ak.shoot()

xsd = Solider(name='许三多')
xsd.gun = ak
xsd.fire()





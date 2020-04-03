"""
房子(House) 有 户型、总面积 和 家具名称列表
    新房子没有任何的家具
家具(HouseItem) 有 名字 和 占地面积，其中
    席梦思(bed) 占地 4 平米
    衣柜(chest) 占地 2 平米
    餐桌(table) 占地 1.5 平米
将以上三件 家具 添加 到 房子 中
打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表
"""


class HouseItem:
    """这是一个家具类"""

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "名称{0}, 面积{1}".format(self.name, self.area)


class House:
    """这是一个家类"""

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        # 户型
        # 总面积
        # 剩余面积
        # 放家具
        return "户型{0},总面积{1},剩余面积{2},放家具{3}".format(self.house_type, self.area, self.free_area,
                                                    self.item_list)

    def add_item(self, item):
        b = bool(self.free_area>item.area)

        if b:
            print('放家具{0}'.format(item))
            self.free_area -= item.area
            self.item_list.append(item.name)
        else:
            print('你剩余面积就{0}要放{1}'.format(self.free_area, item.area))


# 家具
bed = HouseItem('bed', 4)
chest = HouseItem('chest', 2)
table = HouseItem('table', 1.5)

# print(bed)
# print(chest)
# print(table)

# 家
house = House('一室一厅', 2)
house.add_item(bed)
house.add_item(chest)
house.add_item(table)
print(house)




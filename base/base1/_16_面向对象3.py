class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    # str方法必须是有返回字符串类型的
    def __str__(self):
        return "家具%s: ,占地面积%.2f" % (self.name, self.area)


bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

print(bed)
print(chest)
print(table)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return "户型是%s \n总面积是%.2f\n剩余面积%.2f\n家具有%s" \
               % (self.house_type, self.area,
                  self.free_area, self.item_list)

    def add_item(self, house_item):
        if self.free_area < house_item.area:
            print("房子剩余空间%s,不能放下需要空间%.2f的%s"
                  % (self.free_area, house_item.area, house_item.name))
        else:
            self.free_area -= house_item.area
            self.item_list.append(house_item)
            print("添加家具%s成功" % house_item.name)


my_house = House("A", 15)
print(my_house)
my_house.add_item(bed)
my_house.add_item(chest)
my_house.add_item(table)
my_house.add_item(bed)
my_house.add_item(bed)
print(my_house)
for list in my_house.item_list:
    print(list)

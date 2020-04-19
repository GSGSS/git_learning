class Player():  # 定义一个类
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def print_role(self):  # 类的方法
        print("名字是 %s 血量是 %s" % (self.name, self.hp))


user1 = Player('小王', 100)
user2 = Player('小李', 190)
user1.print_role()
user2.print_role()
# 继承


class WarPlayer(Player):
    pass  # 暂时不实现(无薪的实现跟父类一样)


class MasterPlayer(Player):
    def __init__(self, name, hp=333):
        super().__init__(name, hp)


user3 = MasterPlayer('小李儿子')
user3.print_role()

#类型判断
print(type(user1))
print(type(user3))
print(isinstance(user3,Player))
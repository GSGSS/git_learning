import time
chinese_zodiac = "鼠牛虎兔龙蛇马羊猴鸡狗猪"
print(chinese_zodiac[0])

# 序列操作符 成员操作符 in not in  连接操作符
print('狗' in chinese_zodiac)
print('狗' not in chinese_zodiac)

# 连接操作符 +
print("123"+"456")
#重复操作符 *整数
print("123"*3)
#切片操作符 [:]
print(chinese_zodiac[8:-1])
a, b, c = (chinese_zodiac[8:])[:-1]
print(a)
print(b)
print(c)
# 元组语列表，元组是不可编辑的，列表可编辑
yuan = (1, u"我们", 4, 5, 6)
lie = [1, u"我们", 4, 5, 6]
lie[0] = 3
print(lie[0])
print(lie[1])

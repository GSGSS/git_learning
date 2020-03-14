from functools import reduce

# filter 满足条件返回
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = 5
slict = filter(lambda x: x < b, a)
print(type(slict))
print(list(slict))

# map 依次操作每一个参数
a = [1, 2, 3]
map1 = map(lambda x: x+1, a)
print(type(map1))
print(list(map1))
b = [4, 5, 6]
map2 = map(lambda x, y: x+y, a, b)
print(type(map2))
print(list(map2))

# reduce 用初始值跟列表中每一项循环运算得出一个结果
reduce1 = reduce(lambda x, y: x+y, [3, 4, 5], 1)
print(reduce1)

# zip 重新组合数组
zip1 = zip((1, 2, 3), (4, 5, 6))
print(type(zip1))
for i in zip1:
    print(i)
# 用zip对调字典的key和value
# ！！！注意，返回的zip对象是一个迭代器，只能迭代一次
dic1 = {'a': 'aa', 'b': 'bb', 'c': 'cc'}
zip2 = zip(dic1.values(), dic1.keys())
dic2 = dict(zip2)
print(dic2)
# 再次调用zip对象会发现迭代已经完成，无法继续返回结果
dic2 = dict(zip2)
print(dic2)

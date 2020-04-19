# iter
list1 = [1, 2, 3]
it = iter(list1)
print(next(it))
print(next(it))
print(next(it))
# 溢出会报异常
# print(next(it))

# yield 运行到这里返回一个值，下次调用next继续返回
# 用于构建自己的迭代器
# 自定义可支持小数步长的rang函数


def myrange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step


for i in myrange(10, 12, 0.5):
    print(i)
for i in myrange(10, 12, 0.5):
    print(i)

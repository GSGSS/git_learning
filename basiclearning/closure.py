# 普通函数
def sum1(a, b):
    return a+b


# 闭包函数 内部函数引用了外部函数称为闭包
def sumclosure(a):
    def addb(b):
        return a+b
    return addb


fun2 = sumclosure(2)
print(fun2(5))

# 做一个记录调用次数的函数


def counter(begin=0):
    cnt = [begin]

    def add_one():
        cnt[0] += 1
        return cnt[0]
    return add_one


num1 = counter()
print(num1())
print(num1())
num2 = counter(5)
print(num2())
print(num2())


# 例子2 写一个函数解析 ax+b=y
def a_line(a, b):
    def art_y(x):
        return a*x+b
    return art_y


line1=a_line(3,5)
print(line1(10))


#lamda表达式更写发
def b_line(a,b):
    return lambda x: a*x+b

line1=b_line(3,5)
print(line1(10))
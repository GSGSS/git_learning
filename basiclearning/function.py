import re


def func(myname):
    print("function run %s" % (myname))


func('aaa')

# 带参数名的调用


def func2(a, b, c):
    print('a=%s' % a)
    print('b=%s' % b)
    print('c=%s' % c)


func2(1, c=3, b=2)

# 可变长度参数

# 返回参数的个数


def func3(a, *other):
    return 1+len(other)


d = func3('123', '234', '345', 12, 33)
print('d=%s' % d)
e = func3('123')
print('e=%s' % e)

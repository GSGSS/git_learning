import time


#函数上加 @ 装饰函数
# 加上装饰器的函数会被装饰函数包装返回装饰后的函数
def timmer(func1):
    def wrapper():
        start_time = time.time()
        func1()
        stop_time = time.time()
        print('运行时间是 %s秒' % (stop_time-start_time))
    return wrapper


@timmer
def i_can_sleep():
    time.sleep(1)


i_can_sleep()

# 相当于


def i_can_sleep2():
    time.sleep(1)


dec_sleep = timmer(i_can_sleep2)
dec_sleep()


# 带参数的函数装饰器
# 两个数求和 argv是装饰参数
def new_tips(argv):
    # func是装饰的函数
    def tips(func):
        def nei(a, b):
            # func__name__ 取到函数的名字
            print("start %s %s" % (argv, func.__name__))
            func(a, b)
            print("end")
        return nei
    return tips


@new_tips('tipsadd')
def add(a, b):
    print(a+b)


@new_tips('tipssub')
def sub(a, b):
    print(a-b)


add(3, 5)
sub(9, 3)

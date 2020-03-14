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

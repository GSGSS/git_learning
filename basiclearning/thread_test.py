import threading  # python3主要的线程库 _thread是旧版本不推荐
import time
from threading import current_thread


def myTHread(arg1, arg2):
    print(current_thread().getName(), 'start')
    print('%s, %s' % (arg1, arg2))
    time.sleep(3)
    print(current_thread().getName(), 'stop')


# 循环开5个线程
for i in range(1, 6, 1):
    t1 = threading.Thread(target=myTHread, args=(i, i+1))
    t1.start()
    print(t1, 'begin')

print(current_thread().getName(),'end')
import threading
from threading import current_thread
import time


class Mythread(threading.Thread):
    pass


def myTHreadfunc(arg1):
    print(current_thread().getName(), 'start')
    print('%s' % (arg1))
    time.sleep(3)
    print(current_thread().getName(), 'stop')


thread_list = []
# 循环开5个线程
for i in range(1, 6, 1):
    t1 = Mythread(target=myTHreadfunc, args=([i]))
    thread_list.append(t1)

for t in thread_list:
    # setDaemon()在start()之前。在没有用join（主线程不等待的情况）的情况下，非常明显的看到，主线程结束以后，子线程还没有来得及执行，整个程序就退出了。
    t.setDaemon(True)
    t.start()

for t in thread_list:
    t.join()# join的作用 ，主线程一直等待全部的子线程结束之后，主线程自身才继续执行
print(current_thread().getName(), 'end')

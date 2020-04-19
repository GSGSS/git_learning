# 队列  FIFO即First in First Out,先进先出。Queue提供了一个基本的FIFO容器，
# 使用方法很简单,maxsize是个整数，指明了队列中能存放的数据个数的上限。一旦达到上限，
# 插入会导致阻塞，直到队列中的数据被消费掉。如果maxsize小于或者等于0，队列大小没有限制。
# https://www.runoob.com/python3/python3-multithreading.html
from queue import Queue

# q = queue.Queue(5)
# for i in range(1, 5, 1):
#     q.put(i)
# for i in range(1, 5, 1):
#     print(q.get())

import time
import random
from threading import Thread, current_thread

q = Queue(5)


class ProducerThread(Thread):
    def run(self):
        name = current_thread().getName()
        nums = range(100)
        global q
        while True:
            num = random.choice(nums)
            q.put(num)
            print('生产者 %s 生产了数据 %s' % (name, num))
            t = random.randint(1, 3)
            time.sleep(t)
            print('生产者 %s 休息 %s秒' % (name, t))


class ConsumerTread(Thread):
    def run(self):
        name = current_thread().getName()
        global q
        while True:
            num = q.get()
            q.task_done()
            print('消费者 %s消费了%s' % (name, num))
            t = random.randint(1, 5)
            time.sleep(t)
            print('生产者 %s 休息 %s秒' % (name, t))


p1 = ProducerThread(name='p1')
p1.start()
c1 = ConsumerTread(name='c1')
c1.start()

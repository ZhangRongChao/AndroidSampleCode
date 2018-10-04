
"""经典生产者消费者问题（多线程Condition版）"""

"""
    经典生产者与消费者问题：
假设有一群生产者（Producer）和一群消费者（Consumer）通过一个市场来交换产品。
生产者的策略是：如果市场上剩余的产品少于20个，那么就生产4个产品放到市场上；
消费者的策略是：如果市场上剩余的产品多于10个，那么就从市场上消费3个产品。
"""
from threading import Thread, Condition
import time

count = 0
con = Condition()

class Producer(Thread):
    def run(self):
        global count, con
        while True:
            con.acquire()
            if count < 20:
                count += 4
                print("%s：生产者生产了4个，当前总共%d个" % (self.name, count))
                con.notify()
                print('%s：通知等待池中的某个线程，使其可以获得锁' % self.name)
            else:
                print("%s：不生产，等待" % self.name)
                con.wait()
                print('%s：被通知的线程获得了锁' % self.name)
            print('%s：释放锁' % self.name)
            con.release()
            time.sleep(2)

class Consumer(Thread):
    def run(self):
        global count, con
        while True:
            con.acquire()
            if count > 10:
                count -= 3
                print('%s：消费者消费了3个，当前总共%d个' % (self.name, count))
                con.notify()
                print('%s：通知等待池中的某个线程，使其可以获得锁' % self.name)
            else:
                print('%s：不消费，等待' % self.name)
                con.wait()
                print('%s：被通知的线程获得了锁' % self.name)
            print('%s：释放锁' % self.name)
            con.release()
            time.sleep(2)

for i in range(3):
    Producer().start()

for i in range(3):
    Consumer().start()

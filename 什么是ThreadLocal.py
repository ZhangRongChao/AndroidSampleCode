
"""进程间通信之Manager"""

"""
    如果想要实现进程之间的通信，Manager也是常见的实现方式之一。
    与共享内存相比，Manager更加灵活，因为它可以支持多种对象类型，包括：list、dict、Value、
Array、Namespace, Lock、RLock、Semaphore、BoundedSemaphore、Condition、Event、
Barrier、Queue等。此外，Manager还可以通过网络被不同计算机上的进程所共享。但是，Manager的速度
比共享内存要慢。
"""
from multiprocessing import Process, Manager

def f():
    d[1] = 18
    d['2'] = 56
    l.reverse()

manager = Manager()

# 通过Manager创建一个用于进程间通信的字典
d = manager.dict()
# 通过Manager创建一个用于进程间通信的列表
l = manager.list(range(5))

p = Process(target=f)
p.start()
p.join()

print(d)
print(l)

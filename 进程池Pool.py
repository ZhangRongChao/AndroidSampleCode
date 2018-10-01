
"""进程池Pool"""

"""
    如果并发的任务数过多，一次性创建与启动大量的进程会给计算机带来很大的压力，那么就可以使用进程池
对创建与启动的进程进行限制和管理。
    进程池中所能容纳的进程数目是固定的。当需要创建与启动一个子进程时，如果进程池还没满，则会
创建与启动一个子进程并添加到进程池中；如果进程池已经满了，则会一直等待，直到进程池中有任意一个
子进程结束从而腾出一个位置，才会创建与启动一个子进程并添加到进程池中。
    标准库模块multiprocessing中提供了一个类对象Pool，用于表示进程池。进程池中所能容纳的进程数目
可以在创建Pool实例对象时进行指定；如果不指定，默认大小是CPU的核数。
"""
from multiprocessing import Pool
import time, random

print('父进程启动')

def do_sth(i):
    print('子进程%d启动' % i)

    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()

    print('子进程%d结束，耗时%.2f秒' % (i, end - start))

# 将进程池中所能容纳的最大进程数指定为3
pp = Pool(3)

for i in range(1, 11):
    # 与方法start()类似，不同的是，创建并启动由进程池管理的子进程
    pp.apply_async(do_sth, args=(i,))   # 异步
    # pp.apply(do_sth, args=(i,))       # 同步

# 调用方法join()之前必须先调用方法close()
# 调用方法close()之后就不能让进程池再管理新的进程了
pp.close()

# 父进程被阻塞
# 进程池管理的所有子进程执行完之后，父进程再从被阻塞的地方继续执行
pp.join()

print('父进程结束')

# 程序运行后会同时创建并启动3个子进程，第4个子进程要等前面3个中的某一个执行结束后才会创建并启动


"""线程池ThreadPool"""

"""
    如果并发的任务数过多，一次性创建与启动大量的线程会给计算机带来很大的压力，那么就可以使用线程池
对创建与启动的线程进行限制和管理。
    线程池中所能容纳的线程数目是固定的。当需要创建与启动一个子线程时，如果线程池还没满，则会
创建与启动一个子线程并添加到线程池中；如果线程池已经满了，则会一直等待，直到线程池中有任意一个
子线程结束从而腾出一个位置，才会创建与启动一个子线程并添加到线程池中。
    第三方库threadpool中提供了一个类对象ThreadPool，用于表示线程池。线程池中所能容纳的线程数目
可以在创建ThreadPool实例对象时进行指定。
"""
import threadpool, time, random

print('父线程启动')

# 将线程池中所能容纳的最大线程数指定为3
tp = threadpool.ThreadPool(3)

args_list = []
for i in range(1, 11):
    args_list.append(i)

def do_sth(i):
    print('子线程%d启动' % i)

    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()

    print('子线程%d结束，耗时%.2f秒' % (i, end - start))

# 创建需要线程池处理的任务
requests = threadpool.makeRequests(do_sth, args_list)

# 将需要线程池处理的任务全部交给线程池，此后会创建并启动由线程池管理的子线程
for req in requests:
    tp.putRequest(req)

# 父线程被阻塞
# 线程池管理的所有子线程执行完之后，父线程再从被阻塞的地方继续执行
tp.wait()

print('父线程结束')

# 程序运行后会同时创建并启动3个子线程，第4个子线程要等前面3个中的某一个执行结束后才会创建并启动

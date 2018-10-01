
"""阻塞父进程的子进程之方法join()"""

"""
    在父进程中创建并启动子进程后，可以调用子进程的方法join()，这样，子进程会把父进程阻塞，
父进程会等子进程执行完之后再从被阻塞的地方继续执行。
    在调用方法join()时，可以指定参数timeout，从而指定子进程阻塞父进程的时间。
"""
from multiprocessing import Process, current_process
import time

print('父进程%d启动' % current_process().pid)

class MyProcess(Process):
    def run(self):
        print('子进程%d启动' % current_process().pid)
        time.sleep(2)
        print('子进程%d结束' % current_process().pid)

mp = MyProcess()
mp.start()

mp.join()
# mp.join(1)

print('父进程%d结束' % current_process().pid)

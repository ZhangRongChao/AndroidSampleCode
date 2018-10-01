
"""阻塞父线程的子线程之方法join()"""

"""
    在父线程中创建并启动子线程后，可以调用子线程的方法join()，这样，子线程会把父线程阻塞，
父线程会等子线程执行完之后再从被阻塞的地方继续执行。
    在调用方法join()时，可以指定参数timeout，从而指定子线程阻塞父线程的时间。
"""
import threading, time

print('父线程%s启动' % threading.current_thread().getName())

class MyThread(threading.Thread):
    def run(self):
        print('子线程%s启动' % threading.current_thread().getName())
        time.sleep(2)
        print('子线程%s结束' % threading.current_thread().getName())

mt = MyThread()
mt.start()

mt.join()
# mt.join(1)

print('父线程%s结束' % threading.current_thread().getName())

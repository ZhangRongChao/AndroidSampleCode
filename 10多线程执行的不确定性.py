
"""多线程执行的不确定性"""

"""
    默认情况下，进程内所有线程的执行顺序和时间都是不确定的，完全取决于操作系统的调度。
    《图解Python》
"""
import threading, time

def do_sth():
    for i in range(5):
        print('%s：%d' % (threading.current_thread().getName(), i))
        time.sleep(2)

for i in range(3):
    threading.Thread(target=do_sth).start()

do_sth()


"""全局变量在进程的所有线程中可以共享"""

"""
    进程内的所有线程共享内存空间，所以，全局变量在进程的所有线程中可以共享。
    《图解Python》
"""
from threading import Thread

num = 18

def do_sth():
    global num
    num += 1

t = Thread(target=do_sth)
t.start()
t.join()

print(num)    # 19

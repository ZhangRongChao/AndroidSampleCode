
"""定时器线程Timer"""

from threading import Timer
from time import sleep

"""
    如果想要在指定的时间片段之后再创建与启动子线程，可以使用标准库模块threading提供的
类对象Timer，用于表示定时器线程。

    Timer是Thread的子类，除了继承了方法start()用于启动线程之外，还添加了以下方法：
（1）__init__(self, interval, function, args=None, kwargs=None)
    参数interval用于指定在多少秒之后启动线程。由于多线程执行的不确定性，未必恰好在指定的时间之后
启动线程。
    参数function用于指定被方法run()调用的函数或lambda表达式。
    参数args用于指定function接收的位置参数，用元组表示，默认不接收位置参数。
    参数kwargs用于指定function接收的关键字参数，用字典表示，默认不接收关键字参数。
（2）cancel(self)
    在参数interval指定的时间内取消定时器，不再启动线程。

    
def do_sth():
    print('Hello Timer!')

timer = Timer(2, do_sth)
timer.start()
"""

"""
    定时器只执行一次。如果需要每隔一段时间执行一次，则需要在参数function指定的函数或lambda表达式
的内部再次创建与启动定时器线程。
"""
def do_sth():
    print('Hello Timer!')
    global timer
    timer = Timer(3, do_sth)
    timer.start()

timer = Timer(2, do_sth)
timer.start()

sleep(10)
timer.cancel()

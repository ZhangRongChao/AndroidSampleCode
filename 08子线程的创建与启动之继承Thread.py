
"""子线程的创建与启动之继承Thread"""

"""
    使用类对象Thread创建并启动子线程的第2种方式为：
（1）自定义继承自Thread的类对象，重写特殊方法__init__()和方法run()；
（2）根据自定义的类对象创建线程实例对象；
（3）调用线程实例对象的方法start()启动线程。
    调用方法start()后，会自动调用重写后的方法run()。
    
    与第1种方式相比，相当于把参数target指定的函数的函数体转移到了方法run()中。因此，在创建
线程实例对象时无需再指定参数target。
    第1种方式创建线程实例对象时指定的其它参数，在第2种方式中可以传递给重写后的特殊方法__init__()。
    《图解Python》
"""
import threading, time

print('父线程%s启动' % threading.current_thread().getName())

class MyThread(threading.Thread):
    def __init__(self, name, args):
        super().__init__(name=name)
        self.args = args

    def run(self):
        print('子线程%s启动' % threading.current_thread().getName())
        time.sleep(2)
        print('arg1 = %d，arg2 = %d' % self.args)
        print('子线程%s结束' % threading.current_thread().getName())

mt = MyThread(name='mythread', args=(5, 8))
mt.start()

print('父线程%s结束' % threading.current_thread().getName())

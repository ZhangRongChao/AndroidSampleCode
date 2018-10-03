
"""什么是ThreadLocal"""

"""
    ThreadLocal是一个全局变量，用来存放各个线程的局部变量。ThreadLocal中会维护
"某个线程 - 该线程内的某个局部变量名 - 该局部变量的值"的映射。
    在线程中将局部变量写入ThreadLocal的语法格式为：threadlocal.局部变量名 = 局部变量值；
在线程中从ThreadLocal中读取局部变量的语法格式为：threadlocal.局部变量名。

    ThreadLocal常见的应用场景是：为每个线程都绑定一个HTTP请求或数据库连接，绑定的相关信息作为
局部变量，这样线程内的所有相关函数都可以方便地访问这些局部变量。
"""
import threading

thread_local = threading.local()

def do_sth(arg1, arg2, arg3):
    thread_local.local_var1 = arg1
    thread_local.local_var2 = arg2
    thread_local.local_var3 = arg3

    fun1()
    fun2()
    fun3()

def fun1():
    print('%s：%s -- %s -- %s' % (threading.current_thread().name,
                        thread_local.local_var1,
                        thread_local.local_var2,
                        thread_local.local_var3))
def fun2():
    print('%s：%s -- %s -- %s' % (threading.current_thread().name,
                        thread_local.local_var1,
                        thread_local.local_var2,
                        thread_local.local_var3))
def fun3():
    print('%s：%s -- %s -- %s' % (threading.current_thread().name,
                        thread_local.local_var1,
                        thread_local.local_var2,
                        thread_local.local_var3))

t1 = threading.Thread(target=do_sth, args=('a', 'b', 'c'))
t2 = threading.Thread(target=do_sth, args=('d', 'e', 'f'))

t1.start()
t2.start()


"""为什么需要ThreadLocal"""

"""
    多线程操作共享的全局变量是不安全的。那局部变量呢？
    局部变量只归某个线程私有，其它线程是无法访问的。但是，在线程内操作局部变量也存在问题：
如果线程内有多个函数都需要访问多个局部变量local_var1、local_var2...local_varn，则需要
将这些局部变量都作为实参分别传递给这些函数。这样，传递参数就会很麻烦。
"""
import threading

def do_sth(arg1, arg2, arg3):
    local_var1 = arg1
    local_var2 = arg2
    local_var3 = arg3

    fun1(local_var1, local_var2, local_var3)
    fun2(local_var1, local_var2, local_var3)
    fun3(local_var1, local_var2, local_var3)

def fun1(local_var1, local_var2, local_var3):
    print('%s：%s -- %s -- %s' % (threading.current_thread().name,
                           local_var1,
                           local_var2,
                           local_var3))

def fun2(local_var1, local_var2, local_var3):
    print('%s：%s -- %s -- %s' % (threading.current_thread().name,
                           local_var1,
                           local_var2,
                           local_var3))

def fun3(local_var1, local_var2, local_var3):
    print('%s：%s -- %s -- %s' % (threading.current_thread().name,
                           local_var1,
                           local_var2,
                           local_var3))

t1 = threading.Thread(target=do_sth, args=('a', 'b', 'c'))
t2 = threading.Thread(target=do_sth, args=('d', 'e', 'f'))

t1.start()
t2.start()


"""进程池ProcessPoolExecutor（3）"""

"""
    标准库模块concurrent.futures中还提供了两个函数：
（1）wait(fs, timeout=None, return_when=ALL_COMPLETED)
    该函数用于阻塞主进程，以等待指定的Future实例对象序列，直到满足指定的条件。
    参数fs用于指定要等待的Future实例对象序列。
    参数timeout用于指定等待的最长时间。如果指定为None或不指定，则一直等待。
    参数return_when用于指定该函数何时返回，有三种取值：FIRST_COMPLETED、FIRST_EXCEPTION
和ALL_COMPLETED，分别表示：当第一个Future实例对象已经完成或已被取消时、当第一个Future实例对象
抛出异常时、当所有Future实例对象已经完成或已被取消时。
    该函数的返回值是由两个集合组成的元组，第一个集合包含了已经完成或已被取消的所有Future实例对象，
第二个集合包含了没有完成并且没有被取消的所有Future实例对象。
（2）as_completed(fs, timeout=None)
    该函数用于将指定的Future实例对象序列转换为一个迭代器，当序列中的任意一个Future实例对象
已经完成或已被取消时都会被yield。这样，通过遍历得到的迭代器，我们就可以在任意一个Future实例对象
已经完成或已被取消时立即做一些处理，比如调用方法result()得到执行结果。
    参数fs用于指定Future实例对象序列。
    参数timeout用于指定超时时间。如果指定为None或不指定，则不会超时。
    该函数的返回值是Future实例对象的迭代器。
"""
from concurrent.futures import ProcessPoolExecutor, wait, ALL_COMPLETED, \
    FIRST_COMPLETED, as_completed
import time, random

def do_sth(i):
    time.sleep(random.random() * 10)
    return i * i

ppe = ProcessPoolExecutor(max_workers=3)

"""
objs = []
for i in range(1, 5):
    future = ppe.submit(do_sth, i)
    objs.append(future)

#(done, not_done) = wait(objs, return_when=ALL_COMPLETED)
(done, not_done) = wait(objs, return_when=FIRST_COMPLETED)

print(done)
print(not_done)
"""

"""
objs = []
for i in range(1, 5):
    future = ppe.submit(do_sth, i)
    objs.append(future)

future_iterator = as_completed(objs)
for future in future_iterator:
    print(future.result())
"""

"""
    Future提供了一个方法add_done_callback(self, fn)，用于指定Future实例对象已经完成或
已被取消时被立即回调的函数fn，该Future实例对象将作为fn的唯一实参。
    方法add_done_callback()与函数as_completed()都可以实现在Future实例对象已经完成或
已被取消时立即做一些处理的需求。
"""
def get_result(future):
    print(future.result())

for i in range(1, 5):
    future = ppe.submit(do_sth, i)
    future.add_done_callback(get_result)

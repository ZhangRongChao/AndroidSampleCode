
"""进程间通信之共享内存"""

"""
    如果想要实现进程之间的通信，共享内存是常见的实现方式之一。它允许多个进程直接访问同一块内存。
    《图解Python》
    
    共享内存中对象的类型必须是ctypes的。ctypes是与C语言兼容的数据类型。
    
    为了在共享内存中创建ctypes类型的实例对象，标准库模块multiprocessing中提供了如下两个函数：
（1）Value(typecode_or_type, *args, **kwargs)
    返回值表示一个数值。
    参数typecode_or_type用于指定数值的类型码或ctypes类型。
    《图解Python》
（2）Array(typecode_or_type, size_or_initializer, lock=True)
    返回值表示一个数组。
    参数typecode_or_type用于指定数组中元素的类型码或ctypes类型。
    参数size_or_initializer用于指定数组的长度或Python中的数组。
"""
from multiprocessing import Process, Value, Array
import ctypes

# 在共享内存中创建一个表示数值的ctypes对象
num = Value('d', 2.3)
# num = Value(ctypes.c_float, 2.3)

# 在共享内存中创建一个表示数组的ctypes对象
# arr = Array('i', range(1, 5))
arr = Array(ctypes.c_int, range(1, 5))

def do_sth():
    num.value = 1.8
    for i in range(len(arr)):
        arr[i] = -arr[i]

p = Process(target=do_sth)
p.start()
p.join()

print(num.value)    # 1.8
print(arr[:])       # [-1, -2, -3, -4]

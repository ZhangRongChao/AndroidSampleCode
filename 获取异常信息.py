
"""获取异常信息"""

"""
    在捕获异常实例对象后，可以调用标准库模块sys中的函数exc_info以获取异常的相关信息。
    该函数的返回值是一个包含三个元素的元组，这三个元素分别表示：异常的类型、异常的错误信息和
包含异常调用堆栈的跟踪信息的Traceback对象。
    为了进一步提取Traceback对象中包含的信息，可以调用标准库模块traceback中的函数extract_tb。
"""
import sys
import traceback

def f1():
    print(1 / 0)

def f2():
    try:
        f1()
    except ZeroDivisionError:
        ex_type, ex_value, ex_traceback = sys.exc_info()

        print("异常的类型：%s" % ex_type)  # <class 'ZeroDivisionError'>
        print("异常的错误信息：%s" % ex_value)  # division by zero
        print("异常调用堆栈的跟踪信息：%s" % ex_traceback)  # <traceback object at 0x10a106608>

        tb = traceback.extract_tb(ex_traceback)
        print(tb)

        for filename, linenum, funcname, source in tb:
            print("文件名：%s" % filename)
            print("行数：%s" % linenum)
            print("函数名：%s" % funcname)
            print("源码：%s" % source)

f2()



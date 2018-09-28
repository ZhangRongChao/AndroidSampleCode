
"""自动创建与启动的父线程"""

"""
    任何进程都会自动创建并启动一个线程，该线程被称为父（主）线程。
    父（主）线程的默认名称是MainThread。
"""
import threading

# 方法current_thread()用于获得当前线程实例对象（自动创建与启动的父线程）
print('自动创建并启动了父（主）线程：%s' % threading.current_thread().getName())

"""
    在父（主）线程内部，可以手动创建并启动其它子线程。
"""


"""自动创建与启动的进程"""

"""
    当在PyCharm中运行一个py文件时，PyCharm对应的进程会自动创建并启动一个新进程，其默认名称为Python。
当py文件运行结束时，自动创建并启动的新进程也随之结束。
    根据打印的进程id，到任务管理器或活动监视器中找到对应的进程，观察当前进程的创建与消亡。
"""
import os, time
from multiprocessing import current_process

# 方法current_process()用于获得当前进程实例对象（自动创建与启动的进程）
# print(current_process().pid)  # 打印当前进程的id

# getpid：get process id
print(os.getpid())              # 打印当前进程的id

# getppid：get parent process id
print(os.getppid())             # 打印当前进程的父进程的id

time.sleep(20)                  # 让py文件运行至少20秒钟

"""
    在进程的内部，可以手动创建并启动其它子进程。创建并启动子进程的进程被称为父进程。
"""

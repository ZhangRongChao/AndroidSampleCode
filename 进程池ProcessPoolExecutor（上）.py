"""进程池ProcessPoolExecutor（2）"""

"""
    方法submit()的返回值是一个Future实例对象，表示fn的执行。可以调用Future的方法result()
得到fn的返回值。方法result()是一个同步方法，也就是说，直到fn执行完毕之后方法result()才会返回。
"""
from concurrent.futures import ProcessPoolExecutor
import time

"""
def do_sth(i):
    time.sleep(2)
    return i * i

with ProcessPoolExecutor(max_workers=3) as tpe:
    for i in range(1, 5):
        future = tpe.submit(do_sth, i)
        # 同步，需要等待do_sth执行完毕
        print(future.result())
"""

"""
with ProcessPoolExecutor(max_workers=3) as tpe:
    objs = []
    for i in range(1, 5):
        future = tpe.submit(do_sth, i)
        # 异步，无需等待do_sth执行完毕
        print(future)
        objs.append(future)

for obj in objs:
    print(obj.result())
"""

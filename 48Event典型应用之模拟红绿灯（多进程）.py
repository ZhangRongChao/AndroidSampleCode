
"""Event典型应用之模拟红绿灯（多进程）"""

from multiprocessing import Process, Event, current_process
import time

event = Event()

# 红绿灯
def traffic_light():
    count = 0
    while True:
        if count < 5:       # 绿灯亮
            event.set()
            print('%s--绿灯亮'% current_process().name)
        elif count < 10:    # 红灯亮
            event.clear()
            print('%s--红灯亮'% current_process().name)
        else:
            count = 0
        time.sleep(1)
        count += 1

# 车辆
def car():
    while True:
        if event.is_set():      # 绿灯亮
            print('%s--绿灯亮，正在通行' % current_process().name)
            time.sleep(1)
        else:                   # 红灯亮
            print('%s--红灯亮，正在等待' % current_process().name)
            event.wait()
            print('%s--红灯变绿灯，开始通行'% current_process().name)

Process(target=traffic_light, name='红绿灯').start()
Process(target=car, name='车辆1').start()
Process(target=car, name='车辆2').start()

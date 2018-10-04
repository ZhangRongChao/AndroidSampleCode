
"""Event典型应用之模拟红绿灯（多线程）"""

from threading import Thread, Event, current_thread
import time

event = Event()

# 红绿灯
def traffic_light():
    count = 0
    while True:
        if count < 5:       # 绿灯亮
            event.set()
            print('%s--绿灯亮'% current_thread().getName())
        elif count < 10:    # 红灯亮
            event.clear()
            print('%s--红灯亮'% current_thread().getName())
        else:
            count = 0
        time.sleep(1)
        count += 1

# 车辆
def car():
    while True:
        if event.is_set():      # 绿灯亮
            print('%s--绿灯亮，正在通行' % current_thread().getName())
            time.sleep(1)
        else:                   # 红灯亮
            print('%s--红灯亮，正在等待' % current_thread().getName())
            event.wait()
            print('%s--红灯变绿灯，开始通行'% current_thread().getName())

Thread(target=traffic_light, name='红绿灯').start()
Thread(target=car, name='车辆1').start()
Thread(target=car, name='车辆2').start()

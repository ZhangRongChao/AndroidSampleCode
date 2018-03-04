
"""格式化字符串之使用花括号作为占位符"""

"""
    可以调用方法format并使用花括号作为占位符，从而得到格式化字符串。

    更多用法可参考官方文档：
    https://docs.python.org/3/library/string.html#format-string-syntax
    
    《图解Python》
"""
book = '《数据结构与算法》'

s = '买了一本书：{}'.format(book)
print(s)    # 买了一本书：《数据结构与算法》

"""
    如果占位符{}中不指定参数，方法format的参数会按顺序依次匹配所有的占位符{}。
    
    《图解Python》
"""
price = 68.88

s = '花了{}，买了一本书：{}'.format(price, book)
print(s)    # 花了68.88，买了一本书：《数据结构与算法》

"""
    占位符{}中可以指定位置参数，0表示方法format的第1个参数，1表示方法format的第2个参数，...，
依次类推。

    《图解Python》
"""
s = '花了{0}，买了一本书：{1}, 只花了{0}！'.format(price, book)
print(s)  # 花了68.88，买了一本书：《数据结构与算法》, 只花了68.88！


import sys

# 我的iMac运行的平台是：darwin
print('我的{1[computer]}运行的平台是：{0.platform}'.format(sys, {'computer': 'iMac'}))

"""
    可以在方法format中指定关键字参数的名称和值，在占位符{}中指定关键字参数的名称。
    
    《图解Python》
"""
s = '花了{p}，买了一本书：{b}, 只花了{p}！'.format(p=price, b=book)
print(s)  # 花了68.88，买了一本书：《数据结构与算法》, 只花了68.88！


import sys

# 我的iMac运行的平台是：darwin
print('我的{d[computer]}运行的平台是：{system.platform}'.format(system=sys, d={'computer': 'iMac'}))

"""
    占位符{}中可以使用冒号指定整数的表示形式。其中，位置参数或关键字参数的名称放在冒号前面。
"""
# 十进制
print('{:d}'.format(58))        # 58
# 二进制
print('{:b}'.format(58))        # 111010
# 十六进制（a~f是小写）
print('{:x}'.format(58))        # 3a
# 十六进制（A~F是大写）
print('{:X}'.format(58))        # 3A
# 浮点数
print('{:f}'.format(58))        # 58.000000
# 使用逗号作为千位分隔符
print('{:,}'.format(12345678))  # 12,345,678

print('{0:b}'.format(58))       # 111010
print('{num:b}'.format(num = 58)) # 111010

"""
    占位符{}中还可以使用冒号指定宽度。其中，数字是右对齐，字符串是左对齐。
"""
print('{:10}'.format(58))           #         58
print('{:10}'.format('58'))         # 58

print('{0:10}'.format(58))          #         58
print('{num:10}'.format(num = 58))  #         58

"""
    占位符{}中还可以使用冒号指定精度。
"""
# 总共3位
print('{:.3}'.format(3.1415926))            # 3.14
# 小数点后面3位
print('{:.3f}'.format(3.1415926))           # 3.142

print('{:.5}'.format('HelloWorld'))         # Hello

print('{0:.3}'.format(3.1415926))           # 3.14
print('{num:.3}'.format(num = 3.1415926))   # 3.14

# 同时指定宽度和精度
print('{:8.3f}'.format(3.1415926))          #    3.142

"""
    占位符{}中还可以使用冒号指定其它格式。
"""
from datetime import datetime
# 2018-08-18 18:18:18
print('{:%Y-%m-%d %H:%M:%S}'.format(datetime(2018, 8, 18, 18, 18, 18)))

"""
    还可以调用内置函数format得到格式化字符串，它与字符串的方法format是等价的：
'{:x}'.format(y)等价于：format(y, 'x')
"""
print('{:b}'.format(58))                # 111010
print(format(58, 'b'))                  # 111010

print('{:8.3f}'.format(3.1415926))      #    3.142
print(format(3.1415926, '8.3f'))        #    3.142

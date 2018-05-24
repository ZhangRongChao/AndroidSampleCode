
"""调用内置函数dir查看模块的所有属性"""

"""
    见目录"12调用内置函数dir查看模块的所有属性"
"""

"""
    可以调用内置函数dir查看模块的所有属性。

一、调用内置函数dir时模块作为参数
    当调用内置函数dir时如果模块作为参数，会返回指定模块的所有属性。
    其中，以双下划线__开始和结尾的属性是模块的特殊属性。
"""

"""
二、调用内置函数dir时不带任何参数
    当调用内置函数dir时如果不带任何参数，会返回当前模块的局部作用域中的所有属性。
"""
print(dir())
"""
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', 
'__loader__', '__name__', '__package__', '__spec__']
"""

var = 18

def do_sth():
    print('do_sth()被调用')

class MyClass(object):
    pass

print(dir())
"""
['MyClass', '__annotations__', '__builtins__', '__cached__', '__doc__', 
'__file__', '__loader__', '__name__', '__package__', '__spec__', 'do_sth', 'var']
"""

del var
print(dir())
"""
['MyClass', '__annotations__', '__builtins__', '__cached__', '__doc__', 
'__file__', '__loader__', '__name__', '__package__', '__spec__', 'do_sth']
"""

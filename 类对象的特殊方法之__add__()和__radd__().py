"""类对象的特殊方法之__add__()和__radd__()"""

"""
    标准算术运算符在默认情况下不能用于自定义类对象的实例对象。
"""
class MyClass1(object):
    pass

class MyClass2(object):
    pass

# print(MyClass1() + MyClass2())    # TypeError

"""
    如果想让标准算术运算符用于自定义类对象的实例对象，必须在自定义类对象中实现标准算术运算符
对应的以下特殊方法：
1. +对应的特殊方法是__add__()和__radd__();
2. -对应的特殊方法是__sub__()和__rsub__();
3. *对应的特殊方法是__mul__()和__rmul__();
4. /对应的特殊方法是__truediv__()和__rtruediv__();
5. //对应的特殊方法是__floordiv__()和__rfloordiv__()。

    之所以可以使用加法和乘法运算符操作列表，是因为列表对应的类对象list中实现了+和*对应的特殊方法；
之所以可以使用加法和乘法运算符操作字符串，是因为字符串对应的类对象str中也实现了+和*对应的特殊方法。

    假设两个运算数是obj1和obj2，以+为例，对于obj1 + obj2，需要在obj1对应的自定义类对象中实现
特殊方法__add__()，或在obj2对应的自定义类对象中实现特殊方法__radd__()（radd中的r是right的缩写，
因为obj2位于运算符+的右边，所以实现的特殊方法是__radd__()；因为obj1位于运算符+的左边，
所以实现的特殊方法是__add__()）。
    obj1 + obj2的运算流程图为：
    《图解Python》
"""
class C1(object):
    def __add__(self, other):
        print('特殊方法__add__()被调用')
        return 'xxx'
        # return NotImplemented

class C2(object):
    def __radd__(self, other):
        print('特殊方法__radd__()被调用')
        return 'yyy'
        # return NotImplemented

obj1 = C1()
obj2 = C2()

print(obj1 + obj2)

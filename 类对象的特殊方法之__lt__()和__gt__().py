
"""类对象的特殊方法之__lt__()和__gt__()"""

"""
    比较运算符在默认情况下也不能用于自定义类对象的实例。
"""
class MyClass1(object):
    pass

class MyClass2(object):
    pass

# print(MyClass1() < MyClass2())      # TypeError
# print(MyClass1() == MyClass2())     # TypeError

"""
    如果想让比较运算符用于自定义类对象的实例，也必须在自定义类对象中实现比较运算符对应的以下特殊方法：
1. <对应的特殊方法是__lt__()，其中，lt是less than的缩写;
2. >对应的特殊方法是__gt__()，其中，gt是greater than的缩写;
3. <=对应的特殊方法是__le__()，其中，le是less than or equal的缩写;
4. >=对应的特殊方法是__ge__()，其中，le是greater than or equal的缩写;
5. ==对应的特殊方法是__eq__()，其中，eq是equal的缩写；
6. !=对应的特殊方法是__ne__()，其中，ne是not equal的缩写。

    假设两个运算数是obj1和obj2，与obj1 + obj2类似：
1. 对于obj1 < obj2，需要在obj1对应的自定义类对象中实现特殊方法__lt__()，
或在obj2对应的自定义类对象中实现特殊方法__gt__()；
2. 对于obj1 > obj2，需要在obj1对应的自定义类对象中实现特殊方法__gt__()，
或在obj2对应的自定义类对象中实现特殊方法__lt__()；
3. 对于obj1 <= obj2，需要在obj1对应的自定义类对象中实现特殊方法__le__()，
或在obj2对应的自定义类对象中实现特殊方法__ge__()；
4. 对于obj1 >= obj2，需要在obj1对应的自定义类对象中实现特殊方法__ge__()，
或在obj2对应的自定义类对象中实现特殊方法__le__()；
5. 对于obj1 == obj2，需要在obj1对应的自定义类对象中实现特殊方法__eq__()，
或在obj2对应的自定义类对象中实现特殊方法__eq__()；
6. 对于obj1 != obj2，需要在obj1对应的自定义类对象中实现特殊方法__ne__()，
或在obj2对应的自定义类对象中实现特殊方法__ne__()；

    obj1和obj2进行比较运算的运算流程图也与obj1 + obj2的运算流程图相似。
    《图解Python》
"""
class C1(object):
    def __lt__(self, other):
        print('特殊方法__lt__()被调用')
        return True
        # return NotImplemented

class C2(object):
    def __gt__(self, other):
        print('特殊方法__gt__()被调用')
        return True
        # return NotImplemented

obj1 = C1()
obj2 = C2()

print(obj1 < obj2)

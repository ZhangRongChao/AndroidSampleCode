
"""布尔运算符"""

"""
一、什么是布尔运算符
    布尔运算符用于对布尔值进行运算，运算结果仍然是一个布尔值。

    布尔运算符包含如下三个：
    1、and运算符
        当两个运算数都为True时，运算结果才为True。 
"""
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

"""
        and是短路运算符，对于x and y,
            如果x为False，不用计算y，返回x
            如果x为True，返回y
"""
def doSomething() -> int:
    print("函数被调用")
    return 18

print(bool(None))               # False
print(None and doSomething())   # None
print(True and doSomething())   # 18

"""
    2、or运算符
        只要有一个运算数为True，运算结果就为True。
"""
print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False
"""
        or是短路运算符，对于x or y,
            如果x为True，不用计算y，返回x；
            如果x为False，返回y
"""
def doSomething() -> int:
    print("函数被调用")
    return 18

print(bool(56))                 # True
print(56 or doSomething())      # 56
print(False or doSomething())   # 18

"""
    3、not运算符
        用于对运算数取反
            如果运算数为True，运算结果为False。
            如果运算数为False，运算结果为True。
"""
print(not True)    # False
print(not False)   # True

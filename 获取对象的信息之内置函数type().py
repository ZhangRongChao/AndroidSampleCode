
"""获取对象的信息之内置函数dir()"""

"""
    对于指定的类对象或实例对象，可以调用内置函数dir()获得其所有可以访问的属性和方法（包括
从父类中继承的属性和方法）的列表。
    类对象与其实例对象的结果是有区别的，类对象的结果中不包括实例属性。
"""
class MyClass(object):
    ca = 'ca'

    def __init__(self):
        self.ia = 'ia'

    def im(self):
        pass

    @classmethod
    def cm(cls):
        pass

    @staticmethod
    def sm():
        pass

print(dir(MyClass))
"""
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', '__weakref__', 
'ca', 'im', 'cm', 'sm']
"""

print(dir(MyClass()))
"""
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', '__weakref__', 
'ca', 'im', 'cm', 'sm', 'ia']
"""

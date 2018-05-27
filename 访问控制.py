
"""访问控制"""

"""
    访问控制指的是：控制类对象的属性和方法在类对象的外部是否可以直接访问。
    如果在类对象的某个属性或方法前添加两个下划线__，那么在类对象的外部就不能直接访问该属性或方法了。
"""
class MyClass(object):
    def __init__(self):
        self.__pia = 18

    def __pim(self):
        print('__pim()被调用了')

    def do_sth(self):
        print(self.__pia)   # 18
        self.__pim()        # __pim()被调用了

mc = MyClass()

# print(mc.__pia)   # AttributeError: 'MyClass' object has no attribute '__pia'
# mc.__pim()        # AttributeError: 'MyClass' object has no attribute '__pim'

mc.do_sth()

"""
    之所以不能在类的外部直接访问以双下划线开头的属性或方法，是因为：
Python解释器对外把属性或方法__xxx改成了另外一个名字：_类名__xxx。
所以，在类对象的外部仍然可以通过_类名__xxx访问属性或方法__xxx。但是，强烈建议不要这样访问，
因为不同版本的Python解释器可能会把属性或方法__xxx改成不同的名字。
"""
print(mc._MyClass__pia) # 18
mc._MyClass__pim()      # __pim()被调用了

# 调用内置函数dir()获得指定对象所有可以访问的属性和方法
print(dir(mc))
"""
['_MyClass__pia', '_MyClass__pim', 
'__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', '__weakref__', 
'do_sth']
"""

"""
    仍然可以在类对象的外部动态绑定名为__xxx的属性或方法，这与类对象内部名为__xxx的属性或方法
是不同的。
"""
mc.__pia = "Hi"

print(mc.__pia) # Hi

print(dir(mc))
"""
['_MyClass__pia', '_MyClass__pim', 
'__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
'__pia', 
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
'__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
'do_sth']
"""

"""
    除了在类对象的属性或方法前添加两个下划线__，还可以在类对象的属性或方法前添加单下划线_，
这表示：虽然可以在类对象的外部访问该属性或方法，但是最好不要访问。
"""
class SomeClass(object):
    def __init__(self):
        self._pia = 18

    def _pim(self):
        print('_pim()被调用了')

sc = SomeClass()

print(sc._pia)  # 18
sc._pim()       # _pim()被调用了

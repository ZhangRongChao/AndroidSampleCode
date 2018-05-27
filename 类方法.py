
"""类方法"""

"""
    类方法指的是类对象中使用装饰器@classmethod进行装饰的方法。

    在类对象中定义类方法时，必须使用装饰器@classmethod进行装饰，此外，第一个形参表示类对象，
其对应的实参由系统自动传入。第一个形参的名称通常是cls，也可以是其它名称。
    
    类方法可以被类对象所调用，语法格式为：类对象.方法名([实参]) 或：cls.方法名([实参])。
    
    类方法也可以被实例对象所调用，语法格式为：实例对象.方法名([实参]) 或：self.方法名([实参])。
    类对象的所有实例对象都有一个指向类对象的指针，所以，类对象的所有实例对象都可以调用类对象中
定义的类方法。
    
    调用类方法时，系统自动将类对象作为实参传递给第一个形参。第一个实参会传递给第二个形参，
第二个实参会传递给第三个形参，依次类推。

    《图解Python》
"""
class MyClass(object):
    # 在类对象中定义类方法
    @classmethod
    def cm1(cls, p1, p2):
        print(p1, p2)

    # 在类对象中定义类方法
    @classmethod
    def cm2(cls):
        # 通过类对象调用类方法
        # MyClass.cm1(1, 2)
        cls.cm1(1, 2)

    def im(self):
        # 通过实例对象调用类方法
        self.cm1(1, 2)

# 通过类对象调用类方法
MyClass.cm1(1, 2)    # 1 2

mc = MyClass()

# 通过实例对象调用类方法
mc.cm1(1, 2)        # 1 2
mc.cm2()            # 1 2

mc.im()             # 1 2

"""
    在类方法中只能访问类属性，而不能访问实例属性，因为实例属性指的是实例对象所绑定的属性，
当类方法运行时可能还没创建实例对象。
"""
class SomeClass(object):
    ca = 18

    def __init__(self):
        self.ia = 56

    @classmethod
    def cm(cls):
        print(cls.ca)
        # print(SomeClass().ia)

SomeClass.cm()   # 18

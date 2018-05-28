
"""重写"""

"""
    如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其进行重写从而提供自定义的实现，
重写的方式为：在子类中定义与父类中同名的属性或方法（包括装饰器）。
    
    子类重写父类的属性后，通过子类或其实例对象只能访问子类中重写后的属性，而无法再访问父类中
被重写的属性。
    
    子类重写父类的方法后，通过子类或其实例对象只能调用子类中重写后的方法，而无法再调用父类中
被重写的方法。
    父类中被重写的名为xxx的方法，在子类重写后的方法中可以通过super().xxx()进行调用。
"""
class ParentClass(object):
    ca = "ca（父类）"

    def __init__(self):
        print("__init__()被调用了（父类）")

    def im(self):
        print("im()被调用了（父类）")

    @classmethod
    def cm(cls):
        print("cm()被调用了（父类）")

class ChildClass(ParentClass):
    ca = "ca（子类）"

    def __init__(self):
        super().__init__()
        print("__init__()被调用了（子类）")

    def im(self):
        super().im()
        print("im()被调用了（子类）")

    @classmethod
    def cm(cls):
        super().cm()
        print("cm()被调用了（子类）")

cc = ChildClass()       # __init__()被调用了（子类）

print(ChildClass.ca)    # ca（子类）
print(cc.ca)            # ca（子类）

cc.im()                 # im()被调用了（子类）

ChildClass.cm()         # cm()被调用了（子类）
cc.cm()                 # cm()被调用了（子类）

"""
    《图解Python》
    
    MRO的全称是Method Resolution Order（方法解析顺序），它指的是对于一棵类继承树，当调用
最底层类对象的方法时，Python解释器在类继承树上搜索方法的顺序。
    对于一棵类继承树，可以调用最底层类对象的方法mro()或访问最底层类对象的特殊属性__mro__，
获得这棵类继承树的MRO。
"""
class A(object):
    def f(self):
        print('A.f')

class B(A):
    def f(self):
        print('B.f')

class C(A):
    def f(self):
        print('C.f')

class D(B, C):
    def f(self):
        print('D.f')

# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>,
# <class '__main__.A'>, <class 'object'>]
print(D.mro())

# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>,
# <class '__main__.A'>, <class 'object'>)
print(D.__mro__)

d = D()
d.f()       # D.f
# 先把D的方法f()注释掉，再把B的方法f()注释掉，再把C的方法f()注释掉，再把A的方法f()注释掉

"""
    在子类重写后的方法中通过super()调用父类中被重写的方法时，在父类中搜索方法的顺序
基于以该子类为最底层类对象的类继承树的MRO。
    如果想调用指定父类中被重写的方法，可以给super()传入两个实参：super(a_type, obj)，其中，
第一个实参a_type是个类对象，第二个实参obj是个实例对象，这样，被指定的父类是：
obj所对应类对象的MRO中，a_type后面那个类对象。
"""
"""
class A(object):
    def f(self):
        print('A.f')

class B(A):
    def f(self):
        print('B.f')

class C(A):
    def f(self):
        print('C.f')

class D(B, C):
    def f(self):
        super().f()
        # super(D, self).f()    # B.f
        # super(B, self).f()    # C.f
        # super(C, self).f()    # A.f

d = D()
d.f()   # B.f

# 先把B的方法f()注释掉，再把C的方法f()注释掉，再把A的方法f()注释掉
"""

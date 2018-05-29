

"""类的特殊属性之__dict__"""

"""
    对于指定的类对象或实例对象，可以访问特殊属性__dict__获得该类对象或实例对象所绑定的
所有属性和方法的字典。其中，字典中的键为属性名或方法名。
"""
class MyClass(object):
    ca = "ca"

    def __init__(self):
        self.ia = "ia"

    def im(self):
        pass

    @classmethod
    def cm(cls):
        pass

    @staticmethod
    def sm():
        pass

MyClass.ca2 = "ca2"
print(MyClass.__dict__)
"""
{'__module__': '__main__', 
'ca': 'ca', 
'__init__': <function MyClass.__init__ at 0x104613730>, 
'im': <function MyClass.im at 0x1046137b8>, 
'cm': <classmethod object at 0x1046260b8>, 
'sm': <staticmethod object at 0x1046260f0>, 
'__dict__': <attribute '__dict__' of 'MyClass' objects>, 
'__weakref__': <attribute '__weakref__' of 'MyClass' objects>, 
'__doc__': None, 
'ca2': 'ca2'}
"""

mc = MyClass()
mc.ia2 = "ia2"
print(mc.__dict__)   # {'ia': 'ia', 'ia2': 'ia2'}

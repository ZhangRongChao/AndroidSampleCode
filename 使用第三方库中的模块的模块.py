
"""
二、导入模块中的属性
    导入模块中某个属性的语法格式为：from [包名.]模块名 import 属性名。
    同样，如果被导入的模块在一个包结构中，那么必须要通过其所有的父包导航到该模块：
顶层父包名.子包名....子包名。

    导入模块中的属性后，就可以直接访问导入的属性了，而无需添加前缀"[包名.]模块名."，
从而使得代码更加简洁，但是与添加前缀相比，代码的可读性差了一些。
"""
# 操作系统中的所有环境变量
# from os import environ
# print(environ)

# 操作系统中某个指定的环境变量
# from os import getenv
# print(getenv('PYTHON_HOME'))

# MutableMapping类
# from os import MutableMapping
# print(MutableMapping)


# from xml.dom.minidom import StringTypes
# print(StringTypes)

"""
    导入模块中多个属性的语法格式为：from [包名.]模块名 import 属性名1, 属性名2, .. , 属性名n。
"""
# from os import environ, getenv, MutableMapping
# print(environ)
# print(getenv('PYTHON_HOME'))
# print(MutableMapping)

"""
    导入模块中的属性时，可以给导入的属性起一个别名，其语法格式为：
from [包名.]模块名 import 属性名1 as 属性名1的别名, 属性名2 as 属性名2的别名, ... , 
属性名n as 属性名n的别名。 
"""
# from os import environ as er, getenv as ge, MutableMapping as MM
# print(er)
# print(ge('PYTHON_HOME'))
# print(MM)

"""
    可以将模块中的所有属性一次性全部导入，其语法格式为：from [包名.]模块名 import *。

    强烈不推荐这种导入方式，因为：
1. 效率低（将所有的属性全部导入了）
2. 代码的可读性差（不知道具体导入了哪些属性）
3. 容易出错（当两个模块中存在相同的属性时）
"""
from os import *
print(environ)
print(getenv('PYTHON_HOME'))
# print(MutableMapping)

"""
    当导入整个模块时，也可使用类似导入模块中属性的语法格式：from 包名 import 模块名。
"""
from xml.dom import minidom
print(minidom.StringTypes)

"""
    《图解Python》
"""

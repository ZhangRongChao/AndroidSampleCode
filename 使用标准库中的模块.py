
"""使用标准库中的模块"""

"""
    Python官方给我们提供了一个标准库，其中有非常多的模块可供我们使用，用以完成各种不同的任务。

    MacOS系统中标准库的路径：
/Library/Frameworks/Python.framework/Versions/3.x/lib/python3.x
    Windows系统中标准库的路径：
<Python的安装路径>\Lib

    标准库中模块的源代码是极好的Python学习资料。

    标准库中相关模块的使用，可以参考官方文档：
https://docs.python.org/3/library/index.html
    
    如果想要使用标准库中的模块，必须通过import语句进行导入。有两种导入方式：
（1）导入整个模块
（2）导入模块中的属性
"""

"""
一、导入整个模块
    导入整个模块的语法格式为：import [包名.]模块名。
    如果被导入的模块在一个包结构中，那么必须要通过其所有的父包导航到该模块：
顶层父包名.子包名....子包名。
    
    导入整个模块之后，就可以访问模块中的属性了（包括：变量、函数和类），其语法格式为：
[包名.]模块名.属性名。
    
    当输入"[包名.]模块名."之后，在代码提示的下拉列表中，变量用黄色的v（variable）表示，
函数用粉色的f（function）表示，类用蓝色的c（class）表示。
"""
# import os

# 操作系统中的所有环境变量
# print(os.environ)

# 操作系统中某个指定的环境变量
# print(os.getenv('PYTHON_HOME'))

# MutableMapping类
# print(os.MutableMapping)


# import xml.dom.minidom
# print(xml.dom.minidom.StringTypes)

"""
    导入整个模块时，可以给导入的模块起一个别名：import [包名.]模块名 as 模块的别名。
"""
import os as operating_system

# 操作系统中的所有环境变量
# print(operating_system.environ)

# 操作系统中某个指定的环境变量
# print(operating_system.getenv('PYTHON_HOME'))

# MutableMapping类
# print(operating_system.MutableMapping)

# import xml.dom.minidom as md
# print(md.StringTypes)

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

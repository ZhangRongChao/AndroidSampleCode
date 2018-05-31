
"""类对象的特殊属性之__doc__"""

"""
    调用内置函数dir得到的类对象的所有属性中，有一个特殊属性叫__doc__，用于表示类对象的文档字符串。

一、什么是类对象的文档字符串（docstring）
    与"15函数的定义之文档字符串"结合对比着学习。

    与函数的文档字符串类似，位于类对象的第一行的字符串被称为类对象的文档字符串，通常用三个引号表示。
    类对象的文档字符串是对类对象的功能的简要描述。
    
    在PyCharm中，类对象的文档字符串用灰色显示。
    
    之所以称为"文档"字符串，是因为可以使用工具根据文档字符串自动地生成文档。
    
    应该养成编写文档字符串的习惯，以提高程序的可读性。

    按住command键点击内置类对象list以查看其文档字符串。

二、访问类对象的文档字符串
    通过类对象的特殊属性__doc__可以访问类对象的文档字符串。
    调用内置函数help()得到的帮助信息中会包含类对象的文档字符串。
"""
print(list.__doc__)
"""
list() -> new empty list
list(iterable) -> new list initialized from iterable's items
"""

print(help(list))

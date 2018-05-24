

"""模块的特殊属性之__doc__"""

"""
    调用内置函数dir得到的模块所有属性中，有一个特殊属性叫__doc__，用于表示模块的文档字符串。

一、什么是模块的文档字符串（docstring）
    与"15函数的定义之文档字符串"结合对比着学习。
    
    与函数的文档字符串类似，位于模块的第一行的字符串被称为模块的文档字符串，通常用三个引号表示。
    模块的文档字符串是对模块功能的简要描述。
    
    在PyCharm中，模块的文档字符串用灰色显示。
    
    之所以称为"文档"字符串，是因为可以使用工具根据文档字符串自动地生成文档。
    
    应该养成编写文档字符串的习惯，以提高程序的可读性。
    
    打开标准库中的模块base64.py以查看其文档字符串：
    /Library/Frameworks/Python.framework/Versions/3.x/lib/python3.x/base64.py
    <Python的安装路径>\Lib\base64.py
    
二、访问模块的文档字符串
    通过模块的特殊属性__doc__可以访问模块的文档字符串。
    调用内置函数help()得到的帮助信息中会包含模块的文档字符串。
"""
print(__doc__)

import base64
# Base16, Base32, Base64 (RFC 3548), Base85 and Ascii85 data encodings
print(base64.__doc__)

print(help(base64))

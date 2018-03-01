
"""字符串的创建"""

"""
    创建字符串的常见方式有两种：
一、使用引号
    创建字符串时既可以使用单引号，也可以使用双引号，通常使用单引号。
    当把字符串赋值给变量时，变量名不要取名为str，因为str是字符串对应的类名。
>>> s = 'abcd'
>>> s
'abcd'

>>> s = "abcd"
>>> s
'abcd'

# 空字符串
>>> ''
''
>>> ""
''
"""

"""
    可以在单引号中使用双引号，也可以在双引号中使用单引号。
>>> 'abc"def"'
'abc"def"'
>>> "abc'def'"
"abc'def'"
"""

"""
    不能在单引号中使用单引号，也不能在双引号中使用双引号。
    
# 本来想要打印字符串abc'def'，结果前两个单引号进行了匹配
>>> 'abc'def''
  File "<stdin>", line 1
    'abc'def''
           ^
SyntaxError: invalid syntax

# 本来想要打印字符串abc"def"，结果前两个双引号进行了匹配
>>> "abc"def""
  File "<stdin>", line 1
    "abc"def""
           ^
SyntaxError: invalid syntax
"""

"""
二、调用内置函数str（类str的构造方法）

>>> str('abcd')
'abcd'
>>> str("abcd")
'abcd'

>>> str(123)
'123'
>>> str(12.3)
'12.3'

# 空字符串
>>> str()
''
"""

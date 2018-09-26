"""正则表达式的预编译"""

"""
    当在Python中使用正则表达式时，正则表达式会首先被编译。如果一个正则表达式要重复使用多次，
出于效率的考虑，可以预编译该正则表达式，这样，接下来重复使用时就不需要再编译了。

    模块re提供了预编译正则表达式的方法：
compile(pattern[, flags])
    其中，
        参数pattern是一个正则表达式。
        参数flags是一个标志位，与方法match()中参数flags的含义完全相同。
    该方法会返回对正则表达式预编译之后得到的对象。
"""
import re

obj = re.compile(r'...')
# re.compile('...')
print(obj)

"""
    方法compile()的返回值提供了一些方法，在模块re中都有对应的方法。例如：
除了直接调用模块re的方法match()之外，也可以调用模块re的方法compile()的返回值的方法：
match(string[, pos[, endpos]])
其中，
    参数pos用于指定被匹配字符串的起始位置，默认值是0；
    参数endpos用于指定被匹配字符串的结束位置，默认值是字符串的长度。被匹配的子串不包括结束位置。
《图解Python》

    因为在方法compile()中可以指定参数pattern和flags，所以，在调用其返回值的方法时，不需要再指定
参数pattern和flags；而调用模块re中的对应方法时，则需要指定参数pattern和flags。
    模块re的方法match()中的参数pattern和flags被转移到了方法compile()中。
"""
# <re.Match object; span=(0, 3), match='abc'>
print(re.compile(r'...').match('abcde'))
# None
print(re.compile(r'...').match('abcde', 1, 3))

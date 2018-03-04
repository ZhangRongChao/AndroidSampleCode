
"""字符串的反转"""

"""
    与列表不同的是，字符串是不可变类型，因此，如果想对字符串中的所有字符进行反转，
不存在方法reverse，只能调用内置函数reversed。
"""
s = '12345'

iterator = reversed(s)
print(iterator)         # <reversed object at 0x104d1d518>
print(list(iterator))   # ['5', '4', '3', '2', '1']

print(s)                # '12345'

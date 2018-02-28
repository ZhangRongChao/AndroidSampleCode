
"""列表的"查"操作之使用运算符in检查是否存在指定元素"""

"""
    可以使用运算符in（not in）检查列表中是否存在（不存在）指定元素。
"""
L = [3, 4, 5, 6, 7]

print(5 in L)       # True
print(8 in L)       # False

print(5 not in L)   # False
print(8 not in L)   # True

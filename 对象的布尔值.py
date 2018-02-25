
"""对象的布尔值"""

"""
    所有对象都有一个布尔值，可以调用内置函数bool（类bool的构造方法）得到对象的布尔值。

    以下对象的布尔值为False：False、数值零、None、空字符串、空列表、空元组、空字典、空集合。
"""
print(bool(False))      # False

print(bool(0))          # False
print(bool(0.0))        # False

print(bool(None))       # False

print(bool(''))         # False
print(bool(""))         # False

print(bool([]))         # False
print(bool(list()))     # False

print(bool(()))         # False
print(bool(tuple()))    # False

print(bool({}))         # False
print(bool(dict()))     # False

print(bool(set()))          # False
print(bool(frozenset()))    # False

print(bool(18))         # True

print(bool('Python'))   # True
print(bool('    '))     # True

print(bool([1, 2, 3, 4]))   # True
print(bool((1, 2, 3, 4)))   # True

print(bool({'a': 18, 'b': 56}))     # True
print(bool({1, 2, 3, 4}))   # True

"""
    所有对象都可被直接用作布尔值，解释器会自动调用内置函数bool进行转换。
"""
if 18:
    print(18, True)         # 18 True

if 'Python':
    print('Python', True)   # Python True

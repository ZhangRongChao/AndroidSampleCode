
"""深拷贝"""

"""
    可以调用标准库模块copy中的函数deepcopy()实现深拷贝。
"""
import copy

"""
    对于没有嵌套子对象的不可变对象，例如：整数对象、字符串对象和元组对象等，不会进行拷贝，也就是说，
不会创建另一个对象。
"""
i = 18
ic = copy.deepcopy(i)
print(ic)   # 18
print('id(i)：%s' % id(i))       # id(i)：4435749344
print('id(ic)：%s' % id(ic))     # id(ic)：4435749344

t = (1, 2, 3)
tc = copy.deepcopy(t)
print(tc)   # (1, 2, 3)
print('id(t)：%s' % id(t))       # id(t)：4436825504
print('id(tc)：%s' % id(tc))     # id(tc)：4436825504

"""
    所谓深拷贝，指的是：对于某个对象，创建与该对象具有相同值的另一个对象，同时，这两个对象
内部嵌套的对应可变子对象全都不是同一个对象。简单地说，外部和内部都进行了拷贝。
    《图解Python》
"""
L1 = [[3, 6], 8]

import copy # 导入标准库模块copy
L2 = copy.deepcopy(L1)  # 调用标准库模块copy中的函数deepcopy()
print(L2)   # [[3, 6], 8]

print('id(L1)：%s' % id(L1))     # id(L1)：4323826184
print('id(L2)：%s' % id(L2))     # id(L2)：4319457544

print('id(L1[0])：%s' % id(L1[0])) # id(L1)：4323759944
print('id(L2[0])：%s' % id(L2[0])) # id(L2)：4323834056

print('id(L1[1])：%s' % id(L1[1])) # id(L1)：4315834528
print('id(L2[1])：%s' % id(L2[1])) # id(L2)：4315834528

L1[0][1] = 7
L1[1] = 9
print(L1)   # [[3, 7], 9]
print(L2)   # [[3, 6], 8]

"""
    如果不可变对象内部有嵌套的可变子对象，深拷贝之后，会创建一个与该不可变对象具有相同值的另一个对象。
"""
t1 = ([3, 6], 8)

t2 = copy.deepcopy(t1)
print(t2)   # ([3, 6], 8)

print('id(t1)：%s' % id(t1))     # id(t1)：4566993224
print('id(t2)：%s' % id(t2))     # id(t2)：4566999880

print('id(t1[0])：%s' % id(t1[0])) # id(t1)：4567002184
print('id(t2[0])：%s' % id(t2[0])) # id(t2)：4567001864

print('id(t1[1])：%s' % id(t1[1])) # id(t1)：4559014048
print('id(t2[1])：%s' % id(t2[1])) # id(t2)：4559014048

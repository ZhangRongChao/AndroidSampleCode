
"""浅拷贝"""

"""
    对于某个对象，如何创建它的拷贝呢？也就是说，如何创建与该对象具有相同值的另一个对象呢？
"""

"""
    所谓浅拷贝，指的是：对于某个对象，虽然创建了与该对象具有相同值的另一个对象，但是，这两个对象
内部嵌套的对应子对象全都是同一个对象。简单地说，外部进行了拷贝，内部没有拷贝。

    以下方式得到的拷贝都是浅拷贝：
1. 切片操作[:]
2. 调用列表、字典、集合的方法copy()
3. 调用内置函数list()、dict()、set()
4. 调用标准库模块copy中的函数copy()
    《图解Python》
"""
L1 = [[3, 6], 8]

# L2 = L1[:]
# L2 = L1.copy()
# L2 = list(L1)
import copy # 导入标准库模块copy
L2 = copy.copy(L1)  # 调用标准库模块copy中的函数copy()
print(L2)   # [[3, 6], 8]

print('id(L1)：%s' % id(L1))     # id(L1)：4546611720
print('id(L2)：%s' % id(L2))     # id(L2)：4546611784

print('id(L1[0])：%s' % id(L1[0])) # id(L1)：4551329952
print('id(L2[0])：%s' % id(L2[0])) # id(L2)：4551329952

print('id(L1[1])：%s' % id(L1[1])) # id(L1)：4546611720
print('id(L2[1])：%s' % id(L2[1])) # id(L2)：4546611784

L1[0][1] = 7
L1[1] = 9
print(L1)   # [[3, 7], 9]
print(L2)   # [[3, 7], 8]

"""
    对于没有嵌套子对象的不可变对象，例如：整数对象、字符串对象和元组对象等，不会进行拷贝，也就是说，
不会创建另一个对象。
"""
i = 18

ic1 = int(i)
print(ic1)   # 18
print('id(i)：%s' % id(i))       # id(i)：4328729056
print('id(ic1)：%s' % id(ic1))   # id(ic1)：4328729056

ic2 = copy.copy(i)
print(ic2)   # 18
print('id(i)：%s' % id(i))       # id(i)：4328729056
print('id(ic2)：%s' % id(ic2))   # id(ic2)：4328729056


t = (1, 2, 3)

tc1 = tuple(t)
print(tc1)   # (1, 2, 3)
print('id(t)：%s' % id(t))       # id(t)：4332397984
print('id(tc1)：%s' % id(tc1))   # id(tc1)：4332397984

tc2 = copy.copy(t)
print(tc2)   # (1, 2, 3)
print('id(t)：%s' % id(t))       # id(t)：4332397984
print('id(tc2)：%s' % id(tc2))    # id(tc2)：4332397984

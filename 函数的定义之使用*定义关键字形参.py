
"""函数的定义之使用*定义关键字形参"""

"""
    定义函数时，可以在所有形参的某个位置添加一个*，这样，*后面的所有形参都被定义为
只能接收关键字实参的关键字形参。
"""
def f(a, b, *, c, d):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d)

f(1, 2, c = 3, d = 4)   # a = 1 b = 2 c = 3 d = 4
# f(1, 2, 3, 4) # f() takes 2 positional arguments but 4 were given

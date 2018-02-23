
"""函数的调用之使用*将序列中的每个元素都转换为位置实参"""

def f(a, b, c):
    print('a =', a, 'b =', b, 'c =', c)

f(1, 2, 3)  # a = 1 b = 2 c = 3


L = [1, 2, 3]

# 列表L整体作为一个位置实参
# f(L)  # f() missing 2 required positional arguments: 'b' and 'c'

f(L[0], L[1], L[2])  # a = 1 b = 2 c = 3

"""
    调用函数时，可以在序列前面添加一个*，从而将序列中的每个元素都转换为一个单独的位置实参。
"""
# 相当于：f(L[0], L[1], L[2])
f(*L)   # a = 1 b = 2 c = 3

"""
    注意和个数可变的位置形参进行区分。
"""
def fun(*args):
    print(args)

# 列表L整体作为一个位置实参
fun(L)   # ([1, 2, 3],)

# 先将序列中的每个元素都转换为一个单独的位置实参，
# 再用这些位置实参将个数可变的位置形参初始化为一个元组
fun(*L)  # (1, 2, 3)

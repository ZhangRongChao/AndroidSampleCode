
"""只包含一个元素的元组"""

t = (18)
print(t)        # 18
print(type(t))  # <class 'int'>

"""
    元组中至少要包含一个逗号，即使元组只有一个元素，否则，小括号会被看作是数学公式中的小括号。
"""
t = (18,)
# t = 18,
print(t)        # (18,)
print(type(t))  # <class 'tuple'>


"""字典的"查"操作"""

"""
    如果想在字典中根据指定的key查找对应的value，常见的方式有两种：
一、使用中括号

    《图解Python》
"""
d = {'name': 'Jack', 'age': 18}
print(d['name'])        # Jack
"""
    如果字典中不存在指定的key，抛出KeyError。
"""
# print(d['gender'])    # KeyError: 'gender'

"""
二、调用方法get
"""
print(d.get('name'))    # Jack
"""
    可以通过参数设置默认的value，以便在字典中不存在指定的key时将其返回。
"""
print(d.get('gender', '男'))  # 男

"""
    此外，可以使用运算符in（not in）检查字典中是否存在（不存在）指定的key。
"""
print('age' in d)           # True
print('gender' in d)        # False

print('age' not in d)       # False
print('gender' not in d)    # True

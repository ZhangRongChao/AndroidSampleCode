
"""for-in语句"""

"""
一、什么是for-in语句
    for-in语句专门用于遍历序列、字典和集合等类型的对象。
    其中，遍历指的是：把对象的所有元素依次访问一遍。每访问一个元素，称之为一次迭代。因此，
可以使用for-in语句遍历的对象又被称为可迭代对象。
    
    for-in语句的语法格式：
for 自定义的变量 in 要遍历的可迭代对象:
    循环体
其中，循环体对应的代码块必须缩进。
如果循环体内不需要访问自定义的变量，可以将自定义的变量替代为下划线_。
    
    for-in语句的流程图：
    《图解Python》
    
    for-in语句的执行流程：
    反复判断是否遍历完可迭代对象中的所有元素：
如果已经遍历完可迭代对象中的所有元素，则终止循环；
如果没有遍历完可迭代对象中的所有元素，则自定义的变量自动被赋予当前迭代的元素值，然后执行循环体，
执行完循环体后再次判断是否遍历完可迭代对象中的所有元素。
    
    当迭代次数已知时，推荐使用for-in语句；当迭代次数未知时，推荐使用while语句。

二、使用for-in语句遍历range、列表、元组和字符串等序列
"""
for number in range(1, 4):
    print(number)

for _ in range(1, 4):
    print('Hello')

for number in [1, 2, 3]:
    print(number)

for number in (1, 2, 3):
    print(number)

for char in '123':
    print(char)
"""
    在遍历序列的过程中，如果需要对序列进行修改，最好先通过切片操作生成一份序列的拷贝。
"""
words = ['Java', 'Python', 'Kotlin', 'Swift', 'Go']
for word in words[:]:
    if len(word) < 5:
        words.remove(word)
print(words)    # ['Python', 'Kotlin', 'Swift']

"""
三、使用for-in语句遍历集合和字典
"""
s = {2, 3, 1}
for number in s:
    print(number)
for number in sorted(s):
    print(number)


d = {'Fruits': 86, 'Books': 88, 'Videos': 83}

# 遍历字典
# "自定义的变量自动被赋予当前迭代的元素值"中的"元素值"指的是字典的key
for key in d:
    print(key)

print(d.keys())         # dict_keys(['Fruits', 'Books', 'Videos'])
print(list(d.keys()))   # ['Fruits', 'Books', 'Videos']
# 遍历字典的所有key
for key in d.keys():
    print(key)
for key in list(d.keys()):
    print(key)

print(sorted(d))                # ['Books', 'Fruits', 'Videos']
print(sorted(d.keys()))         # ['Books', 'Fruits', 'Videos']
print(sorted(list(d.keys())))   # ['Books', 'Fruits', 'Videos']
# 遍历根据key排序后的字典的所有key
for key in sorted(d):
    print(key)
for key in sorted(d.keys()):
    print(key)
for key in sorted(list(d.keys())):
    print(key)

print(sorted(d, key = d.get))   # ['Videos', 'Fruits', 'Books']
# 遍历根据value排序后的字典的所有key
for key in sorted(d, key = d.get):
    print(key)
print(sorted(d, key = d.get, reverse = True))   # ['Books', 'Fruits', 'Videos']
# 遍历根据value逆序排序后的字典的所有key
for key in sorted(d, key = d.get, reverse = True):
    print(key)

print(d.values())       # dict_values([96, 78, 83])
print(list(d.values())) # [96, 78, 83]
# 遍历字典的所有value
for value in d.values():
    print(value)
for value in list(d.values()):
    print(value)

print(sorted(d.values()))       # [78, 83, 96]
print(sorted(list(d.values()))) # [78, 83, 96]
# 遍历根据value排序后的字典的所有value
for value in sorted(d.values()):
    print(value)
for value in sorted(list(d.values())):
    print(value)

print(d.items()) # dict_items([('Fruits', 86), ('Books', 88), ('Videos', 83)])
print(list(d.items()))  # [('Fruits', 86), ('Books', 88), ('Videos', 83)]
# 遍历字典的所有key-value对
for key, value in d.items():
    print(key, '->', value)
for key, value in list(d.items()):
    print(key, '->', value)

print(sorted(d.items()))    # [('Books', 88), ('Fruits', 86), ('Videos', 83)]
print(sorted(list(d.items()))) # [('Books', 88), ('Fruits', 86), ('Videos', 83)]
# 遍历根据key排序后的字典的所有key-value对
for key, value in sorted(d.items()):
    print(key, '->', value)
for key, value in sorted(list(d.items())):
    print(key, '->', value)

"""
    上面的不全讲，讲的是：
for key in d:
    print(key)
for key in d.keys():
    print(key)
for value in d.values():
    print(value)
for key, value in d.items():
    print(key, '->', value)
"""

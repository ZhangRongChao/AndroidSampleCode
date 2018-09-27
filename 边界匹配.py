
"""边界匹配"""

"""
    边界匹配主要用于匹配字符串的边界或字符串中单词的边界。
    《图解Python》
"""
import re

# ['12']
print(re.findall(r'^\d+', '12-3\n45-6\n78-9'))

# ['12', '45', '78']
print(re.findall(r'^\d+', '12-3\n45-6\n78-9', re.M))

# ['12']
print(re.findall(r'\A\d+', '12-3\n45-6\n78-9', re.M))

# ['9']
print(re.findall(r'\d+$', '12-3\n45-6\n78-9'))

# ['3', '6', '9']
print(re.findall(r'\d+$', '12-3\n45-6\n78-9', re.M))

# ['9']
print(re.findall(r'\d+\Z', '12-3\n45-6\n78-9', re.M))


# ['py']
print(re.findall(r'\bpy\b', 'ab py cd'))
# ['py']
print(re.findall(r'\bpy\b', 'ab#py@cd'))
# ['py', 'py']
print(re.findall(r'\bpy\b', 'py cd py'))

# ['pybc']
print(re.findall(r'\Bpy\w+', 'apy apybc pyb'))

"""
    模块re的方法match()实现的是"不完全匹配"，如果想要实现"完全匹配"，可以在正则表达式式的末尾
添加$。
"""
# <re.Match object; span=(0, 4), match='1234'>
print(re.match(r'\d+', '1234abc'))

# None
print(re.match(r'\d+$', '1234abc'))
# <re.Match object; span=(0, 4), match='1234'>
print(re.match(r'\d+$', '1234'))

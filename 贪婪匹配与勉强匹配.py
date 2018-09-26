
"""贪婪匹配与勉强匹配"""

"""
    贪婪匹配：在匹配正则表达式时，使用尽可能长的子串去匹配。
    勉强匹配：在匹配正则表达式时，使用尽可能短的子串去匹配。

    贪婪匹配和勉强匹配的语法格式：
《图解Python》
"""
import re

# <re.Match object; span=(0, 7), match='abbbbbb'>
print(re.match(r'ab*', 'abbbbbbc'))
# <re.Match object; span=(0, 1), match='a'>
print(re.match(r'ab*?', 'abbbbbbc'))

# <re.Match object; span=(0, 7), match='abbbbbb'>
print(re.match(r'ab+', 'abbbbbbc'))
# <re.Match object; span=(0, 2), match='ab'>
print(re.match(r'ab+?', 'abbbbbbc'))

# <re.Match object; span=(0, 2), match='ab'>
print(re.match(r'ab?', 'abbbbbbc'))
# <re.Match object; span=(0, 1), match='a'>
print(re.match(r'ab??', 'abbbbbbc'))

# <re.Match object; span=(0, 4), match='abbb'>
print(re.match(r'ab{3}', 'abbbbbbc'))
# <re.Match object; span=(0, 4), match='abbb'>
print(re.match(r'ab{3}?', 'abbbbbbc'))

# <re.Match object; span=(0, 7), match='abbbbbb'>
print(re.match(r'ab{3,}', 'abbbbbbc'))
# <re.Match object; span=(0, 4), match='abbb'>
print(re.match(r'ab{3,}?', 'abbbbbbc'))

# <re.Match object; span=(0, 6), match='abbbbb'>
print(re.match(r'ab{3,5}', 'abbbbbbc'))
# <re.Match object; span=(0, 4), match='abbb'>
print(re.match(r'ab{3,5}?', 'abbbbbbc'))

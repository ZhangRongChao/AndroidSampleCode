
"""原始字符串"""

"""
    如果不想让字符串中的转义字符生效，可以在字符串前面添加r或R，从而将字符串声明为原始字符串。
"""
print(r'\tC:\\Program Files')       # \tC:\\Program Files
print(R'\tC:\\Program Files')       # \tC:\\Program Files

"""
    原始字符串的最后一个字符不能是反斜杠（最后两个字符都是反斜杠除外），否则会抛出SyntaxError。
"""
# print(r'HelloWorld\') # SyntaxError: EOL while scanning string literal
print(r'HelloWorld\\')  # HelloWorld\\


# 解释器不会把r'What\'看作是一个字符串，因为原始字符串不能以反斜杠结尾
print(r'What\'s your name')   # What\'s your name

# 解释器会把'What\\'看作是一个字符串，因为原始字符串可以以两个反斜杠结尾
# print(r'What\\'s your name')

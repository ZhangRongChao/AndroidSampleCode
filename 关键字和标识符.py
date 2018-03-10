
"""关键字和标识符"""

"""
一、关键字
    所谓关键字，就是Python语言定义的、具有特殊用途的单词。
    
    通过调用内置函数help()查看所有关键字：
    >>> help()
    Welcome to Python 3.6's help utility!
    ......
    help> keywords
    Here is a list of the Python keywords.  Enter any keyword to get more help.
    False               def                 if                  raise
    None                del                 import              return
    True                elif                in                  try
    and                 else                is                  while
    as                  except              lambda              with
    assert              finally             nonlocal            yield
    break               for                 not                 
    class               from                or                  
    continue            global              pass
    
    通过导入模块keyword查看所有关键字：
    >>> import keyword
    >>> keyword.kwlist
    ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 
    'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 
    'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
    'return', 'try', 'while', 'with', 'yield']
    
二、标识符
    所谓标识符，就是给程序中的变量、函数、方法、类等命名的名字。
    
    标识符的命名规则（必须这样命名）：
    （1）区分大小写
    （2）不能是关键字
    （3）不能以数字开头
    （4）不能包含空格、制表符、数学符号、中划线、箭头等
    
    标识符的命名规范（推荐这样命名）：
    （1）“见名知意”，由一个或多个有意义的单词组合而成。
        计算科学中最难的两件事是命名和缓存失效。
    （2）所有单词全部小写，单词之间用下划线进行分隔。
        例如：student_name, return_result。
"""
# 标识符区分大小写
i = 3
I = 5
print(i)    # 3
print(I)    # 5

# 标识符不能是关键字
# def = 8

# 标识符不能以数字开头
# 5i = 18

# 标识符不能包含空格
# i 5 = 18

# 标识符不能包含制表符
# i   5 = 18

# 标识符不能包含数学符号
# i+5 = 18
# i*5 = 18

# 标识符不能包含中划线
# i-5 = 18

# 标识符不能包含箭头
# i↑5 = 18
# i→5 = 18

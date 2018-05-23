
"""解释器搜索模块的路径"""

"""
    见目录"08解释器搜索模块的路径"

    当使用import语句导入模块时，如果模块没有被导入，首先，解释器按照某种路径搜索模块。

一、解释器搜索模块路径的示例
    拷贝my_module.py并进行修改。

二、解释器搜索模块的路径
    解释器搜索模块的路径存放在模块sys的变量path中。
    
    在交互式命令行中执行：
    >>> import sys
    >>> sys.path
    ['', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', 
    '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6', 
    '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', 
    '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages']
    
    搜索路径主要由三部分组成：
    1. 当前目录
    2. 标准库的目录
    3. 第三方库的安装目录

三、修改解释器搜索模块的路径
    第一种方式：直接修改sys.path
        根据上述打印结果可知，sys.path是一个列表。
        可以在代码运行时直接修改sys.path以修改搜索路径，但是在代码运行后修改会失效。
"""
import sys
sys.path.insert(0, '/Users/zhangrongchao/Downloads')
"""
        把my_module.py拷贝到目录/Users/zhangrongchao/Downloads，并做如下修改：
        def f():
            print('f被调用（Downloads目录）')
"""
import my_module
my_module.f()       # f被调用（Downloads目录）
"""
        在交互式命令行中执行：
        >>> import sys
        >>> sys.path
        搜索路径不变。
    
    第二种方式：设置环境变量PYTHONPATH以修改sys.path
        环境变量PYTHONPATH对应的路径会被自动添加到sys.path中。
        修改后的搜索路径在代码运行后仍然有效。
        
    《图解Python》
"""

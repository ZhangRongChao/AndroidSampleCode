
"""关闭文件"""

"""
    文件在使用完毕后必须要关闭，这是因为文件对象会占用操作系统的资源，并且操作系统在某一时刻
所能打开的文件数量也是有限的。
    读文件或写文件时都有可能产生异常，从而导致方法close()不会被调用。为了保证方法close()
总能被调用，可以把读文件或写文件的操作放在try语句块中，把方法close()的调用放在finally从句中，
伪代码如下：
打开文件
try:
    读文件或写文件
finally：
    调用方法close()关闭文件
    
    由于文件对象实现了特殊方法__enter__()和__exit__()，所以文件对象可以作为上下文管理器。
其中，特殊方法__enter__()返回打开的文件对象，特殊方法__exit__()中关闭打开的文件，因此，
上面的伪代码可以使用with语句来实现：
with 打开文件 as 变量：
    读文件或写文件
"""
with open('myfile.txt', 'w') as file:
    file.write('hello')

"""
    当with语句体中产生异常时，为了让程序能够继续执行，可以使用try-except语句对抛出的
异常实例对象进行捕获和处理。
"""
try:
    with open('myfile.txt', 'w') as file:
        file.write('hello')
except IOError as err:
    print(err)"""
    写文件之前，必须先打开文件。
    可以调用内置函数open()并以只写方式、追加方式或读写方式打开文件。
返回的文件对象有两个用于写文件的方法：
1. write(text)
    用于将指定的字符串写入到文件中。调用后，会先将指定的字符串写入到缓存中，手动调用方法
flush()或close()之后，或者当写入的数据量大于等于缓存的容量时，缓存中的字符串才会被写入到文件中。
    函数的返回值为写入的字符数，即指定的字符串的长度。

    >>> file = open('myfile.txt', 'w')
    >>> file.write('hello')
    5
    >>> file.write('python')  # 因为没有关闭文件，所以继续写入
    6
    >>> file.flush()  
    >>> file.close()  # 文件在使用完毕后必须要关闭
    
    >>> file = open('myfile.txt', 'a')
    >>> file.write('hello')
    5
    >>> file.write('python')
    6
    >>> file.close()  

2. writelines(seq)
    用于将指定的字符串序列依次写入到文件中。调用后，会先将指定的字符串序列依次写入到缓存中，
手动调用方法flush()或close()之后，或者当写入的数据量大于等于缓存的容量时，缓存中的字符串序列
才会依次被写入到文件中。

    >>> file = open('myfile.txt', 'w')
    >>> file.writelines(['123\n', '456\n', '789'])
    >>> file.close()
"""

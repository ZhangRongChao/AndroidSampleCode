"""
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

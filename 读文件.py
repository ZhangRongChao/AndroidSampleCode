
"""读文件"""

"""
myfile.txt:

1234567890
abcdefghijklmn
opqrstuvwxyz
"""

"""
    读文件之前，必须先打开文件。
    可以调用内置函数open()并以只读方式或读写方式打开文件。返回的文件对象有三个用于读文件的方法：
1. read([size])
    如果不传参数，读到文件尾。
    如果传入参数，size用于指定字节数，
        当指定的字节数小于读到文件尾的字节数时，读取指定的字节数；
        当指定的字节数大于读到文件尾的字节数时，或当指定的字节数小于0时，读到文件尾。
    
    如果文件较大，调用read()一次性读取整个文件会导致内存占用较大，因此，最好多次调用read(size)。
    指定的size不要超过默认缓冲区的大小，否则，可能并不能读取到指定的字节数。通过标准库中
模块io的属性DEFAULT_BUFFER_SIZE可以查看默认缓冲区的大小：
    >>> import io
    >>> io.DEFAULT_BUFFER_SIZE
    8192
    
    >>> file = open('myfile.txt')
    >>> file.read()
    '1234567890\nabcdefghijklmn\nopqrstuvwxyz'
    >>> file.close()  # 文件在使用完毕后必须要关闭
    
    >>> file = open('myfile.txt')
    >>> file.read(12)
    '1234567890\na'
    >>> file.read(30) # 因为没有关闭文件，所以继续读取
    'bcdefghijklmn\nopqrstuvwxyz'
    >>> file.close()
    
    >>> file = open('myfile.txt')
    >>> file.read(12)
    '1234567890\na'
    >>> file.read(-5) # 因为没有关闭文件，所以继续读取  
    'bcdefghijklmn\nopqrstuvwxyz'
    >>> file.close()


2. readline([size])
    如果不传参数，读到行尾。
    如果传入参数，size用于指定字节数，
        当指定的字节数小于读到行尾的字节数时，读取指定的字节数；
        当指定的字节数大于读到行尾的字节数时，或当指定的字节数小于0时，读到行尾。
    总之，最多读到行尾。
    
    >>> file = open('myfile.txt')
    >>> file.readline()
    '1234567890\n'
    >>> file.readline(7)
    'abcdefg'
    >>> file.readline(10)
    'hijklmn\n'
    >>> file.readline(3)
    'opq'
    >>> file.readline(-5)
    'rstuvwxyz'
    >>> file.close()   
   
 
3. readlines([size])
    如果不传参数，读到文件尾，返回每一行组成的列表。
    如果传入参数，size用于指定字节数，
        当指定的字符数小于读到文件尾的字节数时，一直读取到最后一个字符所在行的行尾；
        当指定的字符数大于读到文件尾的字节数时，或当指定的字节数小于0时，读到文件尾。
    
    如果文件较大，调用read()一次性读取整个文件会导致内存占用较大，因此，最好多次调用readlines(size)。
    指定的size不要超过默认缓冲区的大小。
        
    >>> file = open('myfile.txt')
    >>> file.readlines()
    ['1234567890\n', 'abcdefghijklmn\n', 'opqrstuvwxyz']
    >>> file.close() 
    
    >>> file = open('myfile.txt')
    >>> file.readlines(8)
    ['1234567890\n']
    >>> file.readlines(50)
    ['abcdefghijklmn\n', 'opqrstuvwxyz']
    >>> file.close()
    
    >>> file = open('myfile.txt')
    >>> file.readlines(8)
    ['1234567890\n']
    >>> file.readlines(-5)
    ['abcdefghijklmn\n', 'opqrstuvwxyz']
    >>> file.close()
"""

"""
    调用内置函数open()并以只读方式或读写方式打开文件后，返回的文件对象是一个迭代器对象，
所以，可以将返回的文件对象直接用于for-in语句，每次迭代都会读取文件中的一行文本。
"""
from collections import Iterator

file = open('myfile.txt')

print(isinstance(file, Iterator))   # True

for line in file:
    print(line)

file.close()

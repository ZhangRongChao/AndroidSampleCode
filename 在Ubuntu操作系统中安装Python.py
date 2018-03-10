
"""在Ubuntu操作系统中安装Python"""

"""
一、系统预装了Python2和Python3
    系统预装的Python2和Python3的路径：/usr/bin

    $ which python2
    /usr/bin/python2

    $ which python3
    /usr/bin/python3

    $ ls -al python*
    python -> python2.7
    python2 -> python2.7
    python2.7
    python3 -> python3.5
    python3.5
    python3.5m
    python3m -> python3.5m

二、使用apt-get下载安装Python3
    $ sudo apt-get install python3 idle3
    $ apt-get --version 或 $ apt-get -v

    安装的Python3可能不是最新版本

三、下载Python3的源代码
    https://www.python.org --> Downloads --> Source code
    --> Latest Python 3 Release - Python 3.x.x

    XZ compressed source tarball
        Python-3.x.x.tar.xz
    Gzipped source tarball
        Python-3.x.x.tgz

四、编译并安装Python3
    1. 解压文件
        $ tar xfz Python-3.6.4.tgz
    2. 切换目录到解压后的文件夹
        $ cd Python-3.6.4
    3. 配置Python3的安装路径
        $ ./configure --prefix=/usr/bin/python3.6.4
    4. 编译Python3的源代码
        $ sudo make
    5. 安装Python3
        $ sudo make install

        可能会出现错误：zlib not available
        $ sudo apt-get install zlib1g
        $ sudo apt-get install zlib1g-dev

        重新执行：sudo make install
    6. 重新建立软链接
        查看软链接：
        $ ls -al python*
        python -> python2.7
        python2 -> python2.7
        python2.7
        python3 -> python3.5
        python3.5
        python3.5m
        python3m -> python3.5m

        删除已有的软链接：
        $ sudo rm /usr/bin/python3

        重新建立软链接：
        $ sudo ln -s /usr/bin/python3.6.4/bin/python3.6 /usr/bin/python3

五、验证Python3是否安装成功
    在终端中输入：python3
    如果打印出版本号Python 3.x.x和交互式命令行的提示符>>>，则安装成功
"""

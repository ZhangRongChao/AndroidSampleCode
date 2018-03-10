
"""在MacOS操作系统中安装Python"""

"""
一、系统预装了Python2
    系统预装的Python2的路径：
    /System/Library/Frameworks/Python.framework/Versions

    $ which python2.7
    /usr/bin/python2.7

    $ ls -al python2.7
    python2.7 -> ../../System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7

    我们需要下载安装的是Python3

二、下载Python3的安装程序
    https://www.python.org --> Downloads --> Mac OS X
    --> Latest Python 3 Release - Python 3.x.x

    Mac OS X 64-bit/32-bit installer

三、安装Python3
    安装后，/Applications/Python 3.6文件夹：
        IDLE.app
            一个非常简单的Python IDE（集成开发环境）
        Install Certificates.command
            安装软件认证的命令
        License.rtf
            软件许可协议
        Python Documentation.html
            官方技术手册，html格式的
            对应的官网内容是：https://www.python.org -->
            Documentation --> Python 3.x Docs
        Python Launcher.app
            当双击包含Python代码的可执行文件时，Python Launcher就会自动运行
        Readme.rtf
            该软件安装包的简介
        Update Shell Profile.command
            更新系统的配置文件，以确保Python解释器的位置和相关工具
            被正确地添加到操作系统的路径中
            只需要运行一次就足够了

四、验证Python3是否安装成功
    在终端中输入：python3
    如果打印出版本号Python 3.x.x和交互式命令行的提示符>>>，则安装成功

五、使用Package Manager下载安装Python3
    1. Homebrew，输入：brew install python3
        brew --version
    2. MacPorts，输入：port install python3
        port -v
"""

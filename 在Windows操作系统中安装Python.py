
"""在Windows操作系统中安装Python"""

"""
一、下载Python3的安装程序
    https://www.python.org --> Downloads --> Windows
    --> Latest Python 3 Release - Python 3.x.x

    Download Windows x86 web-based installer
        32位，只有1MB多，运行这个exe文件后，再从网络上下载安装程序
    Download Windows x86 executable installer
        32位，这个可执行的exe文件中包含了完整的安装程序，推荐
    Download Windows x86 embeddable zip file
        32位，可嵌入式的zip压缩文件
    Download Windows x86-64 web-based installer
        64位，只有1MB多，运行这个exe文件后，再从网络上下载安装程序
    Download Windows x86-64 executable installer
        64位，这个可执行的exe文件中包含了完整的安装程序，推荐
    Download Windows x86-64 embeddable zip file
        64位，可嵌入式的zip压缩文件

二、安装Python3
    选中"Add Python 3.x to PATH"
    "Install Now"，或"Customize installation"
    安装后，开始菜单 --> 所有程序 --> Python 3.x文件夹：
        IDLE（Python 3.x 64-bit）
            一个非常简单的Python IDE（集成开发环境）
        Python 3.x（64-bit）
            交互式命令行
            可以用来快速验证编写的代码片段
            输入quit()或exit()退出
            进入交互式命令行还可以在命令行中输入:py
        Python 3.x Manuals（64-bit）
            官方技术手册，chm格式的
            对应的官网内容是：https://www.python.org -->
            Documentation --> Python 3.x Docs
        Python 3.x Module Docs（64-bit）
            系统中所有已安装模块的文档，在浏览器中查看

三、验证Python3是否安装成功
    在命令提示符窗口中输入：python或py
    如果打印出版本号Python 3.x.x和交互式命令行的提示符>>>，则安装成功
    
    为了区分Python2和Python3，把Python3安装目录下的python.exe拷贝一份并将其重命名为python3.exe
    在命令行中输入：python3
    仍然可以打印出版本号Python 3.x.x和交互式命令行的提示符>>>
"""

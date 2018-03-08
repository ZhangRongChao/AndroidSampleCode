
"""猴子吃桃"""

"""
【问题描述】
	猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个。
	第二天早上又将第一天剩下的桃子吃掉一半，又多吃了一个。
	以后每天早上都吃了前一天剩下的一半后又多吃一个。
	到第10天早上想再吃时，发现只剩下一个桃子了。
	求猴子第一天共摘了多少个桃子。

【设计思路】
    设计思路一：递推
        第1天的桃子数是第2天的桃子数加1后的2倍，第2天的桃子数是第3天的桃子数加1后的2倍，......，
	    一般地，第n天的桃子数是第n+1天的桃子数加1后的2倍。
	    设第n天的桃子数是L(n)，则有递推关系L(n) = (L(n + 1) + 1) * 2，且初始条件为：L(10) = 1。
	    根据递推关系和初始条件，L(10) → L(9) → L(8) → ... → L(2) → L(1)。
"""
def monkey_peach1():
    """求猴子第一天共摘了多少个桃子"""
    L = [None] * 11
    # 初始条件为：L(10) = 1
    L[10] = 1

    for n in range(9, 0, -1):
        # 设第n天的桃子数是L(n)，则有递推关系L(n) = (L(n + 1) + 1) * 2
        # 根据递推关系和初始条件，L(10) → L(9) → L(8) → ... → L(2) → L(1)
        L[n] = (L[n + 1] + 1) * 2

    return L[1]

print('猴子第一天共摘了%d个桃子' % monkey_peach1())

"""
    设计思路二：递归
	    设计思路一的递推关系可看做在一个函数体的内部又调用了该函数。
	    设计思路一的初始条件可看做递归结束条件（递归出口）。
"""
def monkey_peach2(day):
    """求猴子第一天共摘了多少个桃子"""
    # 递归结束条件（递归出口）：L(10) = 1
    if day == 10:
        return 1
    else:
        # 递推关系L(n) = (L(n + 1) + 1) * 2可看做在一个函数体的内部又调用了该函数
        return (monkey_peach2(day + 1) + 1) * 2

print('猴子第一天共摘了%d个桃子' % monkey_peach2(1))

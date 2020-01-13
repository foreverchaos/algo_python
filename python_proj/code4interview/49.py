"""
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。

输入描述: 输入一个字符串,包括数字字母符号,可以为空
输出描述: 如果是合法的数值表达则返回该数字，否则返回0
"""


def str_to_int(s):
    length = len(s)
    if length == 0:
        return 0
    else:
        minus = False
        flag = False
        if s[0] == '+':
            flag = True
        if s[0] == '-':
            flag = True
            minus = True
        begin = 0
        if flag:
            begin = 1
        num = 0
        minus = -1 if minus else 1
        for each in s[begin:]:
            if '0' <= each <= '9':
                num = num * 10 + minus * (ord(each) - ord('0'))
            else:
                num = 0
                break
        return num


if __name__ == '__main__':
    string = '123'
    print(str_to_int(string))

"""
求出113的整数中1出现的次数,并算出1001300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
"""


def number_of_1_between_n(n):
    res = 0
    for i in range(n+1):
        new = list(str(i))
        count = new.count('1')
        res = res + count
    return res


def NumberOf1Between1AndN_Solution(n):
    # write code here
    count = 0
    i = 1
    while i <= n:
        a = n / i
        b = n % i
        count += (a+8) / 10 * i + (a % 10 == 1)*(b + 1)
        i *= 10
    return count


if __name__ == '__main__':
    print(NumberOf1Between1AndN_Solution(31056))

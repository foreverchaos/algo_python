from ctypes import *


# def number_of_1(n):
#     if n < -128 or n > 127:
#         return 0
#     number = abs(n)
#     if number == 0:
#         return 0
#     if number == 1:
#         return 1
#     dp = [0] * (number + 1)
#     dp[1] = 1
#     for i in range(2, number+1):
#         is_match_flag = is_match(i)
#         if is_match_flag:
#             dp[i] = 1
#         else:
#             dp[i] = dp[i/2] + i % 2
#
#     if n > 0:
#         return dp[-1]
#     else:
#         return dp[-1] + 1
#
#
# def is_match(n):
#     if n < 1:
#         return False
#     while n > 1:
#         if n % 2 != 0:
#             return False
#         n = n/2
#     return True

"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""


def NumberOf1(n):
    # write code here
    cnt = 0
    while c_int(n).value:
        n = n & (n-1)
        cnt += 1
        print(c_int(n), n)
    return cnt


def ten_to_two(n):
    count = 0
    res = []
    while n >= 1:
        a = n % 2
        n = n//2
        res.insert(0, a)
        if a == 1:
            count += 1
    return count


if __name__ == '__main__':
    print(NumberOf1(-5))
    print(ten_to_two(-5))
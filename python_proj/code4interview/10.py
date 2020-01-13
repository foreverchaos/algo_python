"""
我们可以用 2 * 1 的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2 * 1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""


def rect_cover(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]


if __name__ == '__main__':
    results = rect_cover(10)
    print(results)
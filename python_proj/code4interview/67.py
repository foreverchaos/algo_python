"""
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为k[0],k[1],...,k[m]。请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
"""


def cut_rope(number):
    if number == 0 or number == 1:
        return 0
    if number == 2:
        return 1
    if number == 3:
        return 2

    dp = [0] * (number + 1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3

    m = 4
    while m <= number:
        t = 0
        for i in range(1, m // 2 + 1):
            t = max(t, dp[i] * dp[m - i])
        dp[m] = t
        m += 1
    return dp[number]


if __name__ == '__main__':
    print(cut_rope(2))
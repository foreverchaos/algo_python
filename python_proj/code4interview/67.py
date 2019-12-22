def cut_rope(number):

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
    print cut_rope(8)
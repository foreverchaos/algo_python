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
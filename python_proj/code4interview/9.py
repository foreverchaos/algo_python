def jump_floor_2(n):
    if n == 0:
        return 0
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        dp[i] = 2 * dp[i-1]

    return dp[-1]


if __name__ == '__main__':
    results = jump_floor_2(1)
    print(results)

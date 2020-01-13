"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""


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

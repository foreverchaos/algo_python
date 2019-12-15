def find_greatest_sum_of_subarray(array):
    if len(array) == 0:
        return 0
    dp = [0] * len(array)
    dp[0] = array[0]
    for i in range(1, len(array)):
        dp[i] = max(dp[i - 1] + array[i], array[i])
    return max(dp)



if __name__ == '__main__':
    n = [6, -3, -2, 7, -15, 1, 2, 2]
    print find_greatest_sum_of_subarray(n)
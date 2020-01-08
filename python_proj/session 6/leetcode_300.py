def max_length_lis(nums):
    size = len(nums)
    if size <= 1:
        return size

    dp = [1] * size

    for i in range(size):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


if __name__ == '__main__':
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    results = max_length_lis(arr)
    print(results)

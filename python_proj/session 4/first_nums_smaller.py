def get_first_nums_smaller_than_target(nums, target):
    if len(nums) == 0:
        return -1
    dp = [False] * len(nums)
    dp[0] = True if nums[0] > target else False
    for i in range(1, len(nums)):
        dp[i] = True if not dp[i-1] and nums[i] > target else False

    for j in range(len(dp)):
        if dp[j]:
            return j


if __name__ == '__main__':
    results = get_first_nums_smaller_than_target([-2, 0, 1, 4, 7, 9, 10], 6)
    print results
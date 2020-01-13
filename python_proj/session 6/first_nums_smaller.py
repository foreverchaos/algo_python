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


def get_first(nums, target):
    if not nums:
        return None
    if nums[0] > target:
        return None
    low, high = 0, len(nums) - 1

    def mid_search(l, h):
        mid = l + (h - l) / 2
        if low >= high:
            return None
        if nums[mid] > target:
            j = mid-1
            while nums[j] > target:
                j -= 1
            return j + 1
        else:
            return mid_search(mid+1, h)

    return mid_search(low, high)


if __name__ == '__main__':
    results = get_first([-2, 0, 1, 4, 7, 9, 10], 2)
    print(results)
"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""


def outer_func(nums, target):
    low, high = 0,  len(arr)-1
    res = [None, None]
    return search_range(nums, target, low, high, res)


def search_range(nums, target, low, high, res):
    if low > high:
        return -1
    mid = low + (high - low)/2
    if nums[mid] == target:
        i, j = mid, mid
        while i >= low:
            if i == 0 or nums[i-1] != target:
                res[0] = i
                break
            i -= 1
        while j <= high:
            if j == high or nums[j+1] != target:
                res[1] = j
                break
            j += 1
    if nums[mid] < target:
        search_range(nums, target, mid+1, high, res)
    elif nums[mid] > target:
        search_range(nums, target, low, mid-1, res)

    return res


if __name__ == '__main__':
    arr = [5, 7, 7, 8, 8, 10]
    low, high = 0, len(arr)-1
    results = outer_func([5, 7, 7, 8, 8, 10], 8)
    print(results)
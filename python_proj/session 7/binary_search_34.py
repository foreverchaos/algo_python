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
    print results
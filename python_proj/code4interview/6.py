def outer(nums):
    low = 0
    high = len(nums)-1
    res = []

    def switch_min(nums, res, low, high):
        mid = low + (high - low) / 2
        if low == high:
            res.append(-1)
            return
        if nums[mid-1] > nums[mid]:
            res.append(nums[mid])
            return

        if nums[mid+1] < nums[mid]:
            res.append(nums[mid+1])
            return
        if nums[mid] > nums[mid-1] and nums[low] > nums[mid]:
            switch_min(nums, res, low, mid-1)
        else:
            switch_min(nums, res, mid+1, high)

    switch_min(nums, res, low, high)
    act_res = [item for item in res if item > 0]
    return act_res[0]


if __name__ == '__main__':
    print outer([3, 4, 5, 1, 2])

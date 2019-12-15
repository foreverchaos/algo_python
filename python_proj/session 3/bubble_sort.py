def bubble_sort(nums):
    for idx in range(len(nums)):
        change = False
        if not change:
            for i in range(len(nums) - idx - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    change = True
    return nums


if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bubble_sort(arr)
    print(sorted_arr)
def insert_sort(nums):
    for idx in range(1, len(nums)):
        current = nums[idx]
        for i, value in enumerate(nums[idx-1::-1]):
            if current < value:
                nums[idx-i], nums[idx-i-1] = nums[idx-i-1], nums[idx-i]

    return nums


def insert_sort_new(nums):
    for i in range(1, len(nums)):
        j = i - 1
        while j >= 0 and nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
            i -= 1
    return nums


if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = insert_sort_new(arr)
    print(sorted_arr)
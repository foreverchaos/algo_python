def insert_sort(nums):
    for idx in range(1, len(nums)):
        current = nums[idx]
        for i, value in enumerate(nums[idx-1::-1]):
            if current < value:
                nums[idx-i], nums[idx-i-1] = nums[idx-i-1], nums[idx-i]

    return nums


if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = insert_sort(arr)
    print(sorted_arr)
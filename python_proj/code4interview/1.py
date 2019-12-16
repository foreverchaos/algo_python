def find(target, nums):
    if target < nums[0][0] or target > nums[-1][-1]:
        return False
    i, j = 0, -1

    def inner_find(i, j):
        if i > len(nums) or j < -len(nums):
            return False
        if target == nums[i][j]:
            return True
        if target > nums[i][j]:
            return inner_find(i+1, j)
        else:
            return inner_find(i, j-1)

    return inner_find(i, j)


if __name__ == '__main__':
    print find(7, [[1, 2, 8, 9], [2, 3, 9, 12], [3, 7, 10, 13], [6, 8, 11, 15]])
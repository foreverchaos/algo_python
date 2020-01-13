"""
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


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
    print(find(7, [[1, 2, 8, 9], [2, 3, 9, 12], [3, 7, 10, 13], [6, 8, 11, 15]]))
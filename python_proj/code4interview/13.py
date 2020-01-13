"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""


def re_order_array(nums):
    s = []
    d = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            d.append(nums[i])
        else:
            s.append(nums[i])
    return s + d


class Solution:
    def reOrderArray(self, array):
        # write code here
        boarder = -1
        for idx in range(len(array)):
            if array[idx] % 2:
                boarder += 1
                array.insert(boarder, array.pop(idx))
        return array


def reorder_list(nums):
    new = sorted(nums, key=lambda a: a % 2 == 0)
    return new


if __name__ == '__main__':
    print(re_order_array([13, 2, 3, 15, 6, 7, 8, 10, 11]))
    print(reorder_list([13, 2, 3, 15, 6, 7, 8, 10, 11]))
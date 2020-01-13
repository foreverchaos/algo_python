"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""


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
        if nums[mid - 1] < nums[mid] < nums[low]:
            switch_min(nums, res, low, mid-1)
        else:
            switch_min(nums, res, mid+1, high)

    switch_min(nums, res, low, high)
    act_res = [item for item in res if item > 0]
    return act_res[0]


if __name__ == '__main__':
    print(outer([3, 4, 5, 1, 2]))

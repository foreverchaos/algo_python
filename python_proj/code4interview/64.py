"""
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}；
针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
"""


def max_in_windows(num, size):
    if size < 1 or size > len(num) or not num:
        return []
    window = [0]
    res = []
    j = 0
    i = 0
    while j < len(num) - size + 1:
        if j > window[-1]:
            window.pop()
            i = j
            window.append(i)
        while i - j < size:
            if num[i] > num[window[-1]]:
                window.pop()
                window.append(i)
            i += 1
        res.append(num[window[-1]])
        j += 1
    return res


def maxInWindows(num, size):
    # write code here
    if size == 0:
        return []
    queue = []
    res = []
    for i in range(len(num)):
        while queue and queue[0] <= i-size:
            queue.pop(0)
        while queue and num[queue[-1]] < num[i]:
            queue.pop(-1)
        queue.append(i)
        if i < size - 1:
            continue
        res.append(num[queue[0]])
    return res


def max_in_windows(nums, size):
    if not nums or len(nums) < size:
        return []
    res = []
    win = []
    for idx, item in enumerate(nums):
        if idx >= size and win[0] <= idx-size:
            win.pop(0)
        while win and nums[win[-1]] <= item:
            win.pop()
        win.append(idx)
        if idx >= size - 1:
            res.append(nums[win[0]])
    return res


if __name__ == '__main__':
    arr = [2, 3, 4, 2, 6, 2, 5, 1]
    print(max_in_windows(arr, 3))
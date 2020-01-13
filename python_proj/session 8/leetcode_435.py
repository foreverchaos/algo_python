"""
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
示例 1:

输入: [ [1,2], [2,3], [3,4], [1,3] ]

输出: 1

解释: 移除 [1,3] 后，剩下的区间没有重叠。
"""


def erase_overlap_intervals(intervals):
    if len(intervals) == 0:
        return 0
    sort_l = sorted(intervals, key=lambda t: t[0])
    dp = [0] * len(sort_l)
    dp[0] = 1
    temp = [sort_l[0]]
    for i in range(1, len(sort_l)):
        temp.append(sort_l[i])
        if temp[-1][0] >= temp[-2][1]:
            dp[i] = dp[i-1] + 1
        else:
            if temp[-1][1] >= temp[-2][1]:
                temp.pop()
            else:
                temp.pop(-2)
            dp[i] = dp[i - 1]

    return len(intervals) - dp[-1]


if __name__ == '__main__':
    a = [[1, 2], [2, 3], [3, 4], [1, 3]]
    b = [[1, 100], [11, 22], [1, 11], [2, 12]]
    results = erase_overlap_intervals(a)
    print(results)
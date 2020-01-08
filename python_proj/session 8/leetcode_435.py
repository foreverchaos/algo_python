
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
    results = erase_overlap_intervals(b)
    print(results)
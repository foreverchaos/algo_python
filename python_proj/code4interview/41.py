"""
他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
"""


def find_continuous_sequence(tsum):
    end = tsum/2
    res = []
    temp = []
    i = 1
    while i <= end + 2:
        while sum(temp) > tsum:
            temp.pop(0)
        while sum(temp) <= tsum:
            if sum(temp) == tsum:
                if len(temp) > 1:
                    temp_res = temp[:]
                    res.append(temp_res)
            temp.append(i)
            i = i + 1

    return res


def find_continuous_seq_for_sun(target):
    windows = []
    for i in range(target):
        windows.append(i)
        while sum(windows) > target:
            windows.pop(0)
            if sum(windows) == target:
                yield windows


if __name__ == '__main__':
    print(find_continuous_sequence(9))

"""
一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。
"""

from collections import Counter


def find_nums_appear_once(array):
    counter = Counter(array)
    res = counter.most_common()[-2:]
    return [x[0] for x in res]


def find_nums_appear_once_new(array):
    res = {}
    for item in array:
        res[item] = 1 if item not in res else res[item] + 1

    results = [k for k, v in res.items() if v == 1]
    return results


if __name__ == '__main__':
    print(find_nums_appear_once_new([1, 1, 2, 2, 3, 4, 4, 6]))
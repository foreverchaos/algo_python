from collections import Counter


def find_nums_appear_once(array):
    counter = Counter(array)
    res = counter.most_common()[-2:]
    return [x[0] for x in res]


def find_nums_appear_once_new(array):
    res = []
    for item in array:
        if item not in res:
            res.append(item)
        else:
            res.remove(item)
    return res


if __name__ == '__main__':
    print find_nums_appear_once_new([1, 1, 2, 2, 3, 4, 4, 6])

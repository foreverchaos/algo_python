def merge_scope(l):
    res = []
    if len(l) == 0:
        return []
    if len(l) == 1:
        return l
    sort_l = sorted(l, key=lambda t: t[0])
    while len(sort_l) > 1:
        if sort_l[0][1] >= sort_l[1][0]:
            if sort_l[0][1] < sort_l[1][1]:
                temp = [sort_l[0][0], sort_l[1][1]]
            else:
                temp = [sort_l[0][0], sort_l[0][1]]
            sort_l.pop(0)
            sort_l.pop(0)
            sort_l.insert(0, temp)
        else:
            res.append(sort_l[0])
            sort_l.pop(0)
    if len(sort_l) == 1:
        res.append(sort_l[-1])
    return res


if __name__ == '__main__':
    a = [1, 3], [2, 6], [8, 10], [15, 18]
    b = [[1, 4], [0, 2], [3, 5]]
    results = merge_scope(b)
    print(results)
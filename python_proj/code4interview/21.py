def is_pop_order(push, out):
    i, j = 0, 0
    res = []
    while i < len(push):
        res.append(push[i])
        if push[i] == out[j]:
            res.pop()
            j = j+1
        i = i + 1

    return res == out[j:][::-1]


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    b = [4, 5, 3, 2, 1]
    c = [4, 3, 5, 1, 2]
    print is_pop_order(a, c)
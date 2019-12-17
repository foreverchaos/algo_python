def ugly_number(index):
    if index <= 0:
        return 0
    if index == 1:
        return 1
    uglys = {1}
    cnt = 0
    i = 0
    while cnt < index-1:
        i += 1
        if i/2.0 in uglys or i/3.0 in uglys or i/5.0 in uglys:
            cnt += 1
            uglys.add(i)

    return i


def ugly_number_new(index):
    res = [1, ]
    a, b, c = 0, 0, 0
    for i in range(1, index):
        ugly = min(res[a] * 2, res[b] * 3, res[c] * 5)
        res.append(ugly)
        if ugly == res[a] * 2:
            a = a + 1
        if ugly == res[b] * 3:
            b = b + 1
        if ugly == res[c] * 5:
            c = c + 1
    return res[-1]


if __name__ == '__main__':
    print ugly_number_new(11)
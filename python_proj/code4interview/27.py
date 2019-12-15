def permutation(ss):
    if len(ss) <= 0:
        return []
    res = []
    perm(ss, res, '')
    uniq = list(set(res))
    return sorted(uniq)


def perm(ss, res, path):
    if ss == '':
        res.append(path)
    else:
        for i in range(len(ss)):
            sub = ss[:i]+ss[i+1:]
            add = path+ss[i]
            perm(sub, res, add)


if __name__ == '__main__':
    s = 'abc'
    print permutation(s)

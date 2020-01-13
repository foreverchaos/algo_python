"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
"""


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
        return
    for i in range(len(ss)):
        sub = ss[:i]+ss[i+1:]
        add = path+ss[i]
        perm(sub, res, add)


if __name__ == '__main__':
    s = 'abc'
    print(permutation(s))

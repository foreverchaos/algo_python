"""
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
"""


def first_not_repest(s):
    if len(s) == 0:
        return -1
    res = []
    repeat = []
    for item in s:
        if item not in res and item not in repeat:
            res.append(item)
        else:
            repeat.append(item)
            if item in res:
                res.remove(item)
    if res:
        return s.index(res[0])
    else:
        return -1


def first_not_repest_char(s):
    # write code here
    map = {}
    for i in range(len(s)):
        map[s[i]] = map.get(s[i], 0) + 1
    for i in range(len(s)):
        if map[s[i]] == 1:
            return i
    return -1


if __name__ == '__main__':
    string = 'googgle'
    print(first_not_repest(string))
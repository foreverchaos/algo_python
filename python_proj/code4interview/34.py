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


def FirstNotRepeatingChar(s):
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
    print first_not_repest(string)
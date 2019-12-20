def str_to_int(s):
    length = len(s)
    if length == 0:
        return 0
    else:
        minus = False
        flag = False
        if s[0] == '+':
            flag = True
        if s[0] == '-':
            flag = True
            minus = True
        begin = 0
        if flag:
            begin = 1
        num = 0
        minus = -1 if minus else 1
        for each in s[begin:]:
            if '0' <= each <= '9':
                num = num * 10 + minus * (ord(each) - ord('0'))
            else:
                num = 0
                break
        return num


if __name__ == '__main__':
    string = '123'
    print str_to_int(string)

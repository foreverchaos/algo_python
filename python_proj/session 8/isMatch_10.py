def is_match(s, p):
    i = 0
    j = 0
    if not s or not p:
        return False

    def loop(s, i, p, j):
        n = len(s)
        m = len(p)
        if j == m:
            return i == n

        if j == m-1 or p[j+1] != '*':
            if i < n and (s[i] == p[j] or p[j] == '.'):
                return loop(s, i+1, p, j+1)
        if j < m-1 and p[j+1] == "*":
            while i < n and (s[i] == p[j] or p[j] == '.'):
                if loop(s, i, p, j+2):
                    return True
                i += 1
            return loop(s, i, p, j + 2)
    return loop(s, i, p, j)


if __name__ == '__main__':
    results = is_match('ab', '.*c')
    print results
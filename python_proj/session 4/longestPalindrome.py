

def longest_palindrome(s):
    if len(s) <= 1:
        return len(s)
    d = {}
    for i in range(len(s) - 1):
        sub1, tmp1 = l_palindrome(s, i, i)
        sub2, tmp2 = l_palindrome(s, i, i+1)
        d[sub1] = tmp1
        d[sub2] = tmp2
    return max(d, key=d.get)


def l_palindrome(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right], right - left - 1


if __name__ == '__main__':
    d = longest_palindrome('bb')
    print d
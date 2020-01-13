"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""


def length_of_longest_substring(s):
    size = len(s)
    if size <= 1:
        return size
    max_len = 0
    window = []
    for i in range(size):
        idx = window.index(s[i]) if s[i] in window else -1
        window.append(s[i])
        if idx < 0:
            if max_len < len(window):
                max_len = len(window)
        else:
            window = window[idx + 1:]
    return max_len


if __name__ == '__main__':
    results = length_of_longest_substring('au')
    print(results)
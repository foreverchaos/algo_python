"""
给定一个字符串s，找到其中最长的回文子序列。可以假设s的最大长度为1000。

示例 1:
输入:

"bbbab"
输出:

4
一个可能的最长回文子序列为 "bbbb"。

示例 2:
输入:

"cbbd"
输出:

2
一个可能的最长回文子序列为 "bb"。
"""


def longest_palindrome(s):
    size = len(s)
    dp = [[0 for _ in range(size)] for _ in range(size)]
    for idx in range(size):
        dp[idx][idx] = 1
    for length in range(2, size + 1):
        for i in range(size-length+1):
            j = i+length-1
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max([dp[i][j-1], dp[i+1][j]])
    return dp[0][size-1]


if __name__ == '__main__':
    results, sub = longest_palindrome('babad')
    print(results, sub)

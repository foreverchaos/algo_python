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

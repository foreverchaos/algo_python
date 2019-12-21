def multiply(A):
    dp = [0] * len(A)
    dp[0] = reduce(lambda x, y: x*y, A[1:])
    dp[len(A) - 1] = reduce(lambda x, y: x*y, A[:len(A)-1])

    for i in range(1, len(dp)-1):
        dp[i] = (reduce(lambda x, y: x*y, A[:i])
                 * reduce(lambda x, y: x*y, A[i+1:]))
    return dp


if __name__ == '__main__':
    print multiply([1, 2, 3, 4, 5, 6])

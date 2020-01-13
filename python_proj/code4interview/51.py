"""
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]A[1]...*A[i-1]A[i+1]...*A[n-1]。不能使用除法。
"""

from functools import reduce


def multiply(A):
    dp = [0] * len(A)
    dp[0] = reduce(lambda x, y: x*y, A[1:])
    dp[len(A) - 1] = reduce(lambda x, y: x*y, A[:len(A)-1])

    for i in range(1, len(dp)-1):
        dp[i] = (reduce(lambda x, y: x*y, A[:i])
                 * reduce(lambda x, y: x*y, A[i+1:]))
    return dp


if __name__ == '__main__':
    print(multiply([1, 2, 3, 4, 5, 6]))

def mySqrt(x: int) -> int:
    left, right, res = 0, x, -1
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid > x:
            right = mid -1
        else:
            res = mid
            left = mid + 1
    return res


if __name__ == '__main__':
    res = mySqrt(0)
    print(res)
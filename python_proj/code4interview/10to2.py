"""
十进制转变成2进制
"""


def ten_to_two(n):
    res = []
    while n >= 1:
        a = n % 2
        n = n//2
        res.insert(0, a)

    return ''.join([str(item) for item in res])


if __name__ == '__main__':
    print(ten_to_two(17))
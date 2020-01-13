"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""


def climb_stars(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return climb_stars(n-1) + climb_stars(n-2)


if __name__ == '__main__':
    print(climb_stars(10))
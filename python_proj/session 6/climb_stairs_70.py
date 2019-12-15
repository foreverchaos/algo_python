def climb_stars(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return climb_stars(n-1) + climb_stars(n-2)


if __name__ == '__main__':
    print(climb_stars(10))
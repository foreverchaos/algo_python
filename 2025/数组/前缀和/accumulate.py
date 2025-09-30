from itertools import accumulate



if __name__ == '__main__':
    l = [2, 3, 4, 5]
    s = list(accumulate(l))
    print(s)
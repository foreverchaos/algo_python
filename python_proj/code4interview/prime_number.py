def get_prime_number(n):
    res = []
    for i in range(n+1):
        flag = True
        mid = i/2
        for j in range(2, mid + 1):
            if i % j == 0:
                flag = False
                break
        if flag:
            res.append(i)

    return res


if __name__ == '__main__':
    print(get_prime_number(100))

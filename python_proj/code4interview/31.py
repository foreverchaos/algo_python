def number_of_1_between_n(n):
    res = 0
    for i in range(n+1):
        new = list(str(i))
        count = new.count('1')
        res = res + count
    return res


def NumberOf1Between1AndN_Solution(n):
    # write code here
    count = 0
    i = 1
    while i <= n:
        a = n / i
        b = n % i
        count += (a+8) / 10 * i + (a % 10 == 1)*(b + 1)
        i *= 10
    return count


if __name__ == '__main__':
    print NumberOf1Between1AndN_Solution(31056)

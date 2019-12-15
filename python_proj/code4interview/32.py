def print_min_number(numbers):
    # write code here
    if len(numbers) == 0:
        return ''

    def compare(a, b):
        res = cmp(str(a) + str(b), str(b) + str(a))
        return res

    min_string = sorted(numbers, cmp=compare)
    return ''.join(str(s) for s in min_string)


if __name__ == '__main__':
    print print_min_number([3, 321, 32])
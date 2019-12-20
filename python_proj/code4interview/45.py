def is_continuous(numbers):
    if not numbers:
        return False
    if 0 not in numbers:
        return sorted(numbers) == sorted([min(numbers) + i for i in range(5)])
    if 0 in numbers:
        flag = False
        while 0 in numbers:
            numbers.remove(0)
        if sorted(set(numbers)) == sorted(numbers):
            if max(numbers) - min(numbers) < 5:
                flag = True
    return flag


if __name__ == '__main__':
    a = [1, 3, 2, 6, 4]
    b = [1, 3, 0, 5, 0]
    print is_continuous(b)

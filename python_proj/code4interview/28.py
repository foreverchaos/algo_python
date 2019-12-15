def more_than_half_num_solution(numbers):
    if len(numbers) == 1:
        return numbers[0]
    nums_copy = []
    i, j = 0, 1
    while j < len(numbers):
        if numbers[i] == numbers[j]:
            nums_copy.append(numbers[i])
        i += 1
        j += 1
    if not nums_copy:
        return 0
    else:
        return nums_copy[0]


if __name__ == '__main__':
    n = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    n = [1, 2, 3, 2, 4, 2, 5, 2, 3]
    print more_than_half_num_solution(n)

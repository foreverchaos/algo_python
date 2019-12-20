def find_numbers_with_sum(array, tsum):
    i, j = 0, len(array) - 1
    res = []
    while i <= j:
        if array[i] + array[j] > tsum:
            j -= 1
        if array[i] + array[j] < tsum:
            i += 1
        if array[i] + array[j] == tsum:
            temp = [array[i], array[j]]
            res.append(temp)
            i += 1
            j -= 1

    return sorted(res, key=lambda x: x[0]*x[1])[0] if res else []


if __name__ == '__main__':
    arr = [1, 2, 4, 7, 11, 16]
    print find_numbers_with_sum(arr, 10)

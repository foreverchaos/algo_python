def print_matrix(matrix):
    l = len(matrix)
    h = len(matrix[0])
    res = []
    temp_flag = [[True for _ in range(h)] for _ in range(l)]
    i, j = 0, 0
    flag = True
    res.append(matrix[0][0])
    temp_flag[0][0] = False
    while flag:
        flag = False
        while j < h-1 and temp_flag[i][j+1]:
            flag = True
            item = matrix[i][j+1]
            res.append(item)
            temp_flag[i][j+1] = False
            j += 1
        while i < l-1 and temp_flag[i+1][j]:
            flag = True
            item = matrix[i+1][j]
            res.append(item)
            temp_flag[i + 1][j] = False
            i += 1
        while j > 0 and temp_flag[i][j-1]:
            flag = True
            item = matrix[i][j-1]
            res.append(item)
            temp_flag[i][j-1] = False
            j -= 1
        while i > 0 and temp_flag[i-1][j]:
            flag = True
            item = matrix[i-1][j]
            res.append(item)
            temp_flag[i-1][j] = False
            i -= 1
    return res


if __name__ == '__main__':
    arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    arr_b = [[1, 2, 3, 4], [5, 6, 7, 8]]
    arr_c = [[1]]
    arr_b = [[1], [2], [3], [4], [5]]
    print print_matrix(arr_b)
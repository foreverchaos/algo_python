def has_path(matrix, rows, cols, path):
    array = list(matrix)
    array = [[a for a in array[i:i + cols]] for i in range(0, rows*cols, cols)]
    start_point = []
    repeat = []
    for i in range(rows):
        for j in range(cols):
            if array[i][j] == path[0]:
                start_point.append((i, j))

    def get_path(i, j, idx):
        if idx >= len(path):
            return True

        for a, b in [(i, j-1), (i, j+1), (i+1, j), (i-1, j)]:
            if 0 <= a <= rows-1 and 0 <= b <= cols-1:
                if array[a][b] == path[idx] and (a, b) not in repeat:
                    repeat.append((a, b))
                    if not get_path(a, b, idx + 1):
                        repeat.remove((a, b))
                    else:
                        return True
        return False

    for i, j in start_point:
        repeat.append((i, j))
        flag = get_path(i, j, 1)
        if not flag:
            repeat.remove((i, j))
        else:
            return True

    return False


if __name__ == '__main__':
    # print(has_path("ABCESFCSADEE", 3, 4, "BCCED"))
    print(has_path("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS", 5, 8, "SGGFIECVAASABCEHJIGQEM"))
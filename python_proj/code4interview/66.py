def moving_count(threshold, rows, cols):
    if threshold < 0:
        return 0
    array = [[True for _ in range(cols)] for _ in range(rows)]
    array[0][0] = False

    def move_next(i, j):
        sum_i = sum([int(s) for s in str(i)])
        sum_j = sum([int(s) for s in str(j)])
        if sum_i + sum_j > threshold:
            return
        else:
            array[i][j] = False

        for a, b in [(i, j-1), (i, j+1), (i+1, j), (i-1, j)]:
            if 0 <= a <= rows-1 and 0 <= b <= cols-1 and array[a][b]:
                move_next(a, b)

    move_next(0, 0)
    return len([item for rows in array for item in rows if not item])


if __name__ == '__main__':
    print moving_count(5, 10, 10)
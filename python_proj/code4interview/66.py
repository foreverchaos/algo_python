"""
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，
每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），
因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
"""


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
    print(moving_count(5, 10, 10))
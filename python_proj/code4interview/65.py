"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，
但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""


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
from typing import List


def generateMatrix(n: int) -> List[List[int]]:
    matrix = [[0]*n for _ in range(n)]
    start_x, start_y, offset, count = 0, 0, 1, 1
    while offset <= n//2:
        for j in range(start_y, n - offset):
            matrix[start_x][j] = count
            count += 1
        for i in range(start_x, n - offset):
            matrix[i][n-offset] = count
            count += 1
        for j in range(n - offset, start_y, -1):
            matrix[n-offset][j] = count
            count += 1
        for i in range(n - offset, start_x, -1):
            matrix[i][start_y] = count
            count += 1
        start_y += 1
        start_x += 1
        offset += 1

    if n%2 == 1:
        matrix[start_x][start_y] = count
    return matrix

if __name__ == '__main__':
    res = generateMatrix(4)
    print(res)
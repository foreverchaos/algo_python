from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    res = []
    start_x, start_y, offset_x, offset_y = 0, 0, 1, 1
    len_x = len(matrix)
    len_y = len(matrix[0])
    visited = [[False] * len_y for _ in range(len_x)]
    if len_x == 1:
        return matrix[0]
    if len_y == 1:
        return [matrix[i][0] for i in range(len_x)]

    while start_y <= len_y - offset_y and start_x <= len_x - offset_x:
        for j in range(start_y, len_y - offset_y):
            res.append(matrix[start_x][j])
            visited[start_x][j] = True
        for i in range(start_x, len_x - offset_x):
            res.append(matrix[i][len_y - offset_y])
            visited[i][len_y - offset_y] = True
        for j in range(len_y - offset_y, start_y, -1):
            if not visited[len_x - offset_x][j]:
                res.append(matrix[len_x - offset_x][j])
        for i in range(len_x - offset_x, start_x, -1):
            if not visited[i][start_y]:
                res.append(matrix[i][start_y])
        if start_y == len_y - offset_y and start_x == len_x - offset_x:
            res.append(matrix[start_x][start_y])
        start_y += 1
        start_x += 1
        offset_x += 1
        offset_y += 1

    return res

if __name__ == '__main__':
    res = spiralOrder([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]])
    print(res)
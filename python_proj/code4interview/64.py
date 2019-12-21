def max_in_windows(num, size):
    if size < 1 or size > len(num) or not num:
        return []
    window = [0]
    res = []
    j = 0
    i = 0
    while j < len(num) - size + 1:
        if j > window[-1]:
            window.pop()
            i = j
            window.append(i)
        while i - j < size:
            if num[i] > num[window[-1]]:
                window.pop()
                window.append(i)
            i += 1
        res.append(num[window[-1]])
        j += 1
    return res


def maxInWindows(num, size):
    # write code here
    if size == 0:
        return []
    queue = []
    res = []
    for i in range(len(num)):
        while queue and queue[0] <= i-size:
            queue.pop(0)
        while queue and num[queue[-1]] < num[i]:
            queue.pop(-1)
        queue.append(i)
        if i < size - 1:
            continue
        res.append(num[queue[0]])
    return res


if __name__ == '__main__':
    arr = [2, 3, 4, 2, 6, 2, 5, 1]
    print maxInWindows(arr, 3)
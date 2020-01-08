from collections import deque, OrderedDict

# def count_smaller(nums):
#     rlst = []
#     for idx, item in enumerate(nums):
#         count = 0
#         for value in nums[idx + 1:]:
#             if value < item:
#                 count += 1
#         rlst.append(count)
#     return rlst


def count_smaller(nums):
    rlst = [0]*len(nums)
    d = {key: value for key, value in enumerate(nums)}
    new_d = list(OrderedDict(sorted(d.items(), key=lambda t: t[1])).keys())
    for idx, item in enumerate(new_d):
        new_deque = deque(new_d[: idx])
        while new_deque:
            if item < new_deque[0]:
                rlst[item] += 1
            new_deque.popleft()
    return rlst


def countSmaller(nums):
    import bisect
    queue = []
    res = []
    for item in nums[::-1]:
        location = bisect.bisect_left(queue, item)
        res.append(location)
        queue.insert(location, item)
    return res[::-1]


if __name__ == '__main__':
    results = countSmaller([5, 2, 6, 1])
    [5, 2, 6, 1]
    [1, 6, 2, 5]

    [(0, 5), (1, 2), (2, 6), (3, 1)]
    [(3, 1), (1, 2), (0, 5), (2, 6)]

    [0, 1, 2, 3]
    [3, 1, 0, 2]
    [2, 1, 1, 0]


    print(results)
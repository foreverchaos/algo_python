from collections import deque


def get_window_max(new_list, k):
    rslt = []
    n = k - 1
    if len(new_list) < k or not new_list:
        return []
    else:
        deque_sub = deque(new_list[:n])
        while n < len(new_list):
            deque_sub.append(new_list[n])
            rslt.append(max(deque_sub))
            deque_sub.popleft()
            n = n + 1
    return rslt


def get_window_max_enhance(nums, k):
    win = []
    ret = []
    if len(nums) < k or not nums:
        return []

    for i, v in enumerate(nums):
        if i >= k and win[0] <= i - k:
            win.pop(0)
        while win and nums[win[-1]] <= v:
            win.pop()
        win.append(i)
        if i >= k - 1:
            ret.append(nums[win[0]])
    return ret


if __name__ == '__main__':
    results = get_window_max_enhance([1, 3, -1, -3, 5, 3, 6, 7], 3)
    # results = get_window_max_enhance([1, -1], 1)
    print(results)
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


# def get_window_max_enhance(nums, k):
#     rslt = []
#     temp = deque([])
#     if len(nums) < k or not nums:
#         return []
#     else:
#         for key, value in enumerate(nums):
#             if not temp:
#                 temp.append(key)
#             elif value > nums[temp[-1]]:
#                 temp.append(key)
#                 temp.popleft()
#             if key >= k:
#                 rslt.append(nums[temp[0]])
#             if key - temp[0] > k:
#                 temp.popleft()


if __name__ == '__main__':
    results = get_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3)
    print(results)
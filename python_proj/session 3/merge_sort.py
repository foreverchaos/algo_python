def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums)/2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:len(nums)])
    return merge(left, right)


def merge(l, r):
    result = []
    i = 0
    j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    result += l[i:]
    result += r[j:]
    return result


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    results = merge_sort(arr)
    print(results)
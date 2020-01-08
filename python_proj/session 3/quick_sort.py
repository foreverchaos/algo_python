def quick_sort(lists, i, j):
    if i >= j:
        return lists
    pivot = lists[i]
    low = i
    high = j
    while i < j:
        while i < j and lists[j] >= pivot:
            j -= 1
        lists[i] = lists[j]
        while i < j and lists[i] <= pivot:
            i += 1
        lists[j] = lists[i]
    lists[j] = pivot
    quick_sort(lists, low, i-1)
    quick_sort(lists, i+1, high)
    return lists


def quick_sort_new(lists, i, j):
    if i >= j:
        return lists
    low = i
    high = j
    while i < j:
        while i < j and lists[j] >= lists[i]:
            j = j - 1
        lists[j], lists[i] = lists[i], lists[j]
        i = i+1
        while i < j and lists[i] <= lists[j]:
            i = i+1
        lists[j], lists[i] = lists[i], lists[j]
        j = j-1
    quick_sort(lists, low, i-1)
    quick_sort(lists, i+1, high)
    return lists


if __name__ == '__main__':
    arr = [30, 24, 5, 58, 18, 36, 12, 42, 39]
    arr1 = [4, 2, 1, 5, 6, 7, 11, 9]
    results = quick_sort_new(arr, 0, len(arr1) - 1)
    print results
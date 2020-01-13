"""
统计一个数字在排序数组中出现的次数。
"""


def get_number_of_k(data, k):
    low = 0
    high = len(data) - 1

    def binary_search(d, low, high):
        if low > high:
            return 0
        mid = low + (high - low) / 2
        if data[mid] == k:
            i = mid - 1
            j = mid + 1
            count = 1
            while i >= low and data[i] == k:
                count += 1
                i -= 1
            while j <= high and data[j] == k:
                count += 1
                j += 1
            return count
        elif data[mid] < k:
            return binary_search(d, mid + 1, high)
        elif data[mid] > k:
            return binary_search(d, low, mid - 1)

    return binary_search(data, low, high)


if __name__ == '__main__':
    print(get_number_of_k([1, 2, 3, 4, 4, 6], 6))

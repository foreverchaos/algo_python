"""
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""


def get_least_numbers(tinput, k):
    l = len(tinput)
    i, j = 0, l-1

    def quick_sort(sub, low, high):
        i = low
        j = high

        if i >= j:
            return

        while i < j:
            while i < j:
                if sub[i] < sub[j]:
                    j -= 1
                else:
                    sub[i], sub[j] = sub[j], sub[i]
                    break
            while i < j:
                if sub[i] < sub[j]:
                    i += 1
                else:
                    sub[i], sub[j] = sub[j], sub[i]
                    break
        std = j
        # if std >= k:
        #     flag = True
        quick_sort(sub, low, std)
        quick_sort(sub, std+1, high)

    return quick_sort(tinput, i, j)


def test_new(tinput, k):

    if len(tinput) < k:
        return []
    tmp = sorted(tinput[:k])
    for item in tinput[k:]:
        i = k - 1
        while i >= 0 and item < tmp[i]:
            i -= 1
        if i < k-1:
            tmp.insert(i + 1, item)
            tmp.pop()

    return tmp


if __name__ == '__main__':
    n = [4, 5, 1, 6, 2, 7, 3, 8]
    print(test_new(n, 4))
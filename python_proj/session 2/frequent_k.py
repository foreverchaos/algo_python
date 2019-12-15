from collections import Counter, OrderedDict


def top_k_frequent_counter(nums, k):
    return [item[0] for item in Counter(nums).most_common(k)]


def top_k_frequent(nums, k):
    d = {}
    for item in nums:
        if item in d.keys():
            d[item] += 1
        else:
            d[item] = 1

    back_items = [[v[1], v[0]] for v in d.items()]
    back_items.sort(reverse=True)
    # return [back_items[i][1] for i in range(0, len(back_items))][:k]

    return list(OrderedDict(sorted(d.items(), key=lambda t: t[1], reverse=True)).keys())[:k]


if __name__ == '__main__':
    results = top_k_frequent(['a', 'a', 'a', 'b', 'b', 'c'], 2)
    print(results)
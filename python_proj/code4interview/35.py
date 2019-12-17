def inverse_pairs(data):
    count = 0
    data_sort = sorted(data)
    copy_sort = data_sort[:]
    for item in copy_sort:
        idx = data.index(item)
        i = data_sort.index(item)
        if idx > i:
            count = count + (idx - i)
        data.remove(item)
        data_sort.remove(item)
    return count


def inverse_pairs_new(data):
    count = 0
    temp = []
    for item in data:
        if temp:
            j = len(temp)-1
            if item > temp[j]:
                temp.append(item)
            else:
                while j >= 0 and item < temp[j]:
                    j -= 1
                    count += 1
                temp.insert(j + 1, item)
        else:
            temp.append(item)
    return count


if __name__ == '__main__':
    target = [364, 637, 341, 406, 747, 995, 234, 971, 571, 219, 993]
    print inverse_pairs_new(target)
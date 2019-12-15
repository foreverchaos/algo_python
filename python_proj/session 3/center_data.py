from copy import deepcopy


def center_data(k):
    if k == 1:
        return ['0', '1', '8']
    if k == 2:
        return ['11', '69', '96', '88']
    if k > 2:
        if k % 2 != 0:
            res = []
            for item in center_data(k-1):
                for j in center_data(1):
                    new = deepcopy(item)
                    new_list = list(new)
                    new_list.insert(len(list(new_list))//2, j)
                    res.append(''.join(new_list))
        else:
            res = []
            add_list = deepcopy(center_data(2))
            add_list.append('00')
            for item in center_data(k - 2):
                for j in add_list:
                    new = deepcopy(item)
                    new_list = list(new)
                    new_list.insert(len(list(new_list))//2, j)
                    res.append(''.join(new_list))
    return res


if __name__ == '__main__':
    results = center_data(3)
    print(results)
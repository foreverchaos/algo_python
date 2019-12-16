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
    target = [364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
    print inverse_pairs_new(target)
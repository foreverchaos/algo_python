def find_continuous_sequence(tsum):
    end = tsum/2
    res = []
    temp = []
    i = 1
    while i <= end + 1:
        while sum(temp) > tsum:
            temp.pop(0)
        while sum(temp) <= tsum:
            if sum(temp) == tsum:
                if len(temp) > 1:
                    temp_res = temp[:]
                    res.append(temp_res)
            temp.append(i)
            i = i + 1

    return res


if __name__ == '__main__':
    print find_continuous_sequence(9)

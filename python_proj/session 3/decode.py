def nums_decode(nums):
    nums_l = list(nums)
    if nums_l[0] == '0':
        return 0
    return decode(nums_l, len(nums_l)-1)


def decode(nums_list, idx):
    if idx <= 0:
        return 1
    count = 0
    curr = int(nums_list[idx])
    prev = int(nums_list[idx-1])
    if curr > 0:
        count = decode(nums_list, idx-1)

    if prev == 1 or (prev == 2 and curr <= 6):
        count += decode(nums_list, idx-2)
    return count


if __name__ == '__main__':
    c = nums_decode('226')
    print(c)
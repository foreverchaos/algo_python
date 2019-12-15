def re_order_array(nums):
    s = []
    d = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            d.append(nums[i])
        else:
            s.append(nums[i])
    return s + d


if __name__ == '__main__':
    print re_order_array([1, 2, 3, 5, 6, 7, 8, 10, 11])
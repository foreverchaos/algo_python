
def numdecode(nums):
    l = list(nums)
    if nums[0] == '0':
        return 0
    else:
        return decode(l, len(nums) - 1)


def decode(num_list, idx):
    if idx <= 0:
        return 1
    count = 0
    if int(num_list[idx]) > 0:
        count = decode(num_list, idx-1)
    if int(num_list[idx - 1]) == 1 or (
            int(num_list[idx]) <= 6 and int(num_list[idx - 1]) == 2):
            count += decode(num_list, idx-2)
    return count


def decode_dynamic(nums):
    l = list(nums)
    if nums[0] == '0':
        return 0
    if len(l) < 2:
        return 1
    dp = [0] * len(l)
    dp[0] = 1
    temp = int(''.join(l[:2]))
    if temp <= 26 and int(l[1]) > 0:
        dp[1] = 2
    if temp <= 26 and int(l[1]) == 0:
        dp[1] = dp[0]
    if temp > 26 and int(l[1]) > 0:
        dp[1] = dp[0]
    if int(l[1]) == 0:
        dp[1] = 0

    for i in range(2, len(l)):
        curr, prev = int(l[i]), int(l[i-1])
        count = 0
        if curr > 0:
            count = dp[i-1]
        if prev == 1 or (prev == 2 and curr <= 6):
            count = count + dp[i-2]
        dp[i] = count
        if curr == 0 and prev > 2:
            dp[i] = 0

    return dp[-1]


if __name__ == '__main__':
    results = decode_dynamic('301')
    print results
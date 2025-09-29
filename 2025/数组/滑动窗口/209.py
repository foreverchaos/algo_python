from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    left, right, sum = 0, 0, 0
    length = len(nums) + 1
    while right < len(nums):
        sum +=nums[right]
        while sum >= target:
            if right-left < length:
                length = right-left+1
            sum -=nums[left]
            left+=1
        right+=1
    if length == len(nums) + 1:
        return 0
    return length


if __name__ == '__main__':
    res = minSubArrayLen(11, [1,2,3,4,5])
    print(res)
from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    left, right, length = 0, 0, 0
    while right < len(nums):
        if nums[right] == nums[left] == 1:
            length = max(length, right - left + 1)
        else:
            left = right if nums[right] != 1 else left + 1
        right += 1
    if nums[-1] == 1:
        length = max(1, length)
    return length

def findMaxConsecutiveOnesSolution(nums: List[int]) -> int:
    length = 0
    count = 0
    for num in nums:
        if num == 1:
            count += 1
            length = max(length, count)
        else:
            count = 0
    return length

if __name__ == '__main__':
    res = findMaxConsecutiveOnesSolution([0,1])
    print(res)
from typing import List

def removeDuplicates(nums: List[int]) -> int:
    slow, fast = 1, 1
    while fast < len(nums):
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow

if __name__ == '__main__':
    res = removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    print(res)
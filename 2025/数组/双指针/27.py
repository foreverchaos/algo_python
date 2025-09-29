from typing import List


def removeElement(nums: List[int], val: int) -> int:
    slow, fast = 0, 0
    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow+=1
        fast+=1
    return slow

if __name__ == '__main__':
    res = removeElement([0,1,2,2,3,0,4,2], 2)
    print(res)
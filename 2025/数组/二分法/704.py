from typing import List


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if target < nums[mid]:
            right = mid
        elif target > nums[mid]:
            left = mid + 1
        elif target == nums[mid]:
            return mid
    return -1

if __name__ == '__main__':
    res = search([2, 5], 5)
    print(res)

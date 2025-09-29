from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    if len(nums) == 0:
        return [-1, -1]
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if target < nums[mid]:
            right = mid
        elif target > nums[mid]:
            left = mid + 1
        elif target == nums[mid]:
            start, end = mid, mid
            while  start >= 0 and nums[start] == target:
                start-=1
            while  end < len(nums) and nums[end] == target:
                end+=1
            return [start + 1, end - 1]

    return [-1, -1]


if __name__ == '__main__':
    res = searchRange([5,7,7,8,8,10], 8)
    print(res)
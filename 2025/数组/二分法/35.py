from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    global mid
    left, right = 0, len(nums)
    if target < nums[left]:
        return 0
    if target > nums[len(nums)-1]:
        return len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if target < nums[mid]:
            right = mid
        elif target > nums[mid]:
            left = mid + 1
        elif target == nums[mid]:
            return mid
    return mid + 1 if nums[mid] < target else mid #重点在这行


if __name__ == '__main__':
    res = searchInsert([1,3,5], 4)
    print(res)
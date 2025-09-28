from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    results = []
    start = 0
    end = len(nums) - 1
    while start <= end:
        if nums[start]**2 > nums[end]**2:
            results.insert(0, nums[start]**2)
            start=start+1
        elif nums[start]**2 < nums[end]**2:
            results.insert(0, nums[end]**2)
            end=end-1
        elif nums[start]**2 == nums[end]**2:
            results.insert(0, nums[start]**2)
            if end != start:
                results.insert(0, nums[end]**2)
            start=start+1
            end=end-1
    return results

if __name__ == '__main__':
    result = sortedSquares([-4,-1,0,3,10])
    print(result)
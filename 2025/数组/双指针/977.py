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


def sortedSquareImproved(nums: List[int]) -> list[float]:
    l, r, i = 0, len(nums)-1, len(nums)-1
    res = [float('inf')] * len(nums) # 需要提前定义列表，存放结果
    while l <= r:
        if nums[l] ** 2 < nums[r] ** 2: # 左右边界进行对比，找出最大值
            res[i] = nums[r] ** 2
            r -= 1 # 右指针往左移动
        else:
            res[i] = nums[l] ** 2
            l += 1 # 左指针往右移动
        i -= 1 # 存放结果的指针需要往前平移一位
    return res

if __name__ == '__main__':
    result = sortedSquares([-4,-1,0,3,10])
    print(result)
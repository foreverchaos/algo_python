"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
"""


def combination_sum(candidates, target):
    size = len(candidates)
    if size == 0:
        return []
    candidates.sort()
    solution = []
    res = []

    def back_track(candidates, begin, size, solution, res, target):
        if target == 0:
            res.append(solution[:])

        for index in range(begin, size):
            residue = target - candidates[index]
            if residue < 0:
                break
            solution.append(candidates[index])
            back_track(candidates, index, size, solution, res, residue)
            solution.pop()

    back_track(candidates, 0, size, solution, res, target)
    return res


if __name__ == '__main__':
    results = combination_sum([2, 3, 6, 7], 7)
    print(results)
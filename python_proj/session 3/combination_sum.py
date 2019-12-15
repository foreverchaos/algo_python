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
    results = combination_sum([3, 2, 6, 7], 7)
    print(results)
def twoSum(nums, target):
    for i in range(len(nums)):
        num = target - nums[i]
        if num in nums[i + 1:]:
            return [i, nums.index(num, i + 1)]


new_list = [2,7,11,15]
target = 9
nums = twoSum(new_list,target)
print(nums)

from collections import defaultdict

a = ["a", "b", "a"]
b = [10, 11, 12]

d = defaultdict(str)
for index, i in enumerate(a):
    d[i] += str(b[index])
print d
print d["c"]

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print dict(d)
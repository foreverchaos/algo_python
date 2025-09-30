from collections import Counter
from typing import List


def totalFruit(fruits: List[int]) -> int:
    temp = []
    count = 0
    left, right = 0, 0
    while right < len(fruits):
        temp.append(fruits[right])
        while len(set(temp)) > 2:
            temp.pop(0)
            left += 1
        count = max(right - left + 1, count)
        right += 1
    return count

def totalFruitCounter(fruits: List[int]) -> int:
    cnt = Counter()
    count = 0
    left, right = 0, 0
    while right < len(fruits):
        cnt[fruits[right]] += 1
        while len(cnt) > 2:
            cnt[fruits[left]] -= 1
            if cnt[fruits[left]] == 0:
                cnt.pop(fruits[left])
            left += 1
        count = max(right - left + 1, count)
        right += 1
    return count

if __name__ == '__main__':
    res = totalFruit([1, 2, 1])
    print(res)
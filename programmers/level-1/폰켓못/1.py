# 5분
from collections import Counter


def solution(nums):
    n = len(nums)
    counter = Counter(nums)
    if len(counter.keys()) > n / 2:
        answer = n / 2
    else:
        answer = len(counter.keys())
    return int(answer)


nums = [3, 3, 3, 2, 2, 4]
print(solution(nums))

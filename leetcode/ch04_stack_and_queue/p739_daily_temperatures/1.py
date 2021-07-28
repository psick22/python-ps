# https://leetcode.com/problems/daily-temperatures/
from typing import List


class Solution:
    # TimeError
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []
        for idx, temp in enumerate(temperatures):
            print(idx, temp)
            cnt = 0
            for day in range(idx + 1, len(temperatures)):
                if temperatures[day] > temp:
                    cnt += 1
                    break
                elif day == len(temperatures) - 1:
                    cnt = 0
                    break
                else:
                    cnt += 1
            answer.append(cnt)
        return answer


temperatures = [
    [73, 74, 75, 71, 69, 72, 76, 73], [30, 40, 50, 60], [30, 60, 90]
]

results = [
    [1, 1, 4, 2, 1, 1, 0, 0], [1, 1, 1, 0], [1, 1, 0]
]

for i, t in enumerate(temperatures):
    print(f'case {i + 1} : {Solution().dailyTemperatures(t)}')

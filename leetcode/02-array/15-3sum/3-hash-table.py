from typing import List
from collections import defaultdict

"""
hash table
time : O(N^2)
space : O(N)

status : Accepted
runtime : 7588 ms
memory : 79.2 MB  

"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        memo = defaultdict(list)
        n = len(nums)
        answer = set()

        for k in range(n):
            memo[nums[k]].append(k)

        for i in range(n):
            for j in range(i + 1, n):
                twoSum = -nums[i] - nums[j]

                for k in memo[twoSum]:
                    if k != i and k != j:
                        answer.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                        break
        return answer


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))

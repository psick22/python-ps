from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        for i in range(0, n, 2):
            res += min(nums[i], nums[i + 1])
        return res


nums = [1, 4, 3, 2]

print(Solution().arrayPairSum(nums))

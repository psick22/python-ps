from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            if (target - num) in nums[idx + 1:]:
                return [idx, nums[idx + 1:].index(target - num) + idx + 1]


nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))

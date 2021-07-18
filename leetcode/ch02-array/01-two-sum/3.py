from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for idx, num in enumerate(nums):
            nums_map[num] = idx

        for idx, num in enumerate(nums):
            if target - num in nums_map and idx != nums_map[target - num]:
                return [idx, nums_map[target-num]]


nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))

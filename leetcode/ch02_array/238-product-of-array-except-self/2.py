from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in nums]

        left = 1
        right = 1

        for i in range(len(nums)):
            res[i] *= left
            res[-1-i] *= right
            left *= nums[i]
            right *= nums[-1-i]

        return res



nums = [-1, 1, 0, -3, 3]
print(Solution().productExceptSelf(nums))

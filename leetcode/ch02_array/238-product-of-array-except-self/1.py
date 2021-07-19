from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        p = 1
        for i in range(len(nums)):
            res.append(p)
            p *= nums[i]

        p = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= p
            p *= nums[i]
        return res


nums = [-1, 1, 0, -3, 3]
print(Solution().productExceptSelf(nums))

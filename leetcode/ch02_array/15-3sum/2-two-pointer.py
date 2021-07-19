from typing import List

"""
two pointer
time : O(N^2)
space : O(1)

status : Accepted
runtime : 868 ms
memory : 17.5 MB  

"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                res = nums[i] + nums[j] + nums[k]

                if res > 0:
                    k -= 1
                elif res < 0:
                    j += 1
                else:
                    answer.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    k -= 1
                    j += 1
        return answer


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))

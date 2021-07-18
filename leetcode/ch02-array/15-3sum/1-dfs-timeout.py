from typing import List

"""
dfs

status : Time Limit Exceeded

"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def dfs(L, s, sum, res):
            if L == 3:
                if sum == 0:
                    if sorted(res) in answer:
                        return
                    answer.append(sorted(res))

            else:
                for i in range(s, len(nums)):
                    res[L] = nums[i]
                    dfs(L + 1, i + 1, sum + nums[i], res)

        dfs(0, 0, 0, [0, 0, 0])
        return answer


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))

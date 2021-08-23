from typing import *
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def rec(nums: List[int], target: int, l: List[int], k: int):
            if(target == 0):
                ans.append(l)
            else:   
                for i in range(k, n):
                    if(target - nums[i] >= 0):
                        rec(nums, target-nums[i], l + [nums[i]], i)
        rec(candidates, target, [], 0)
        return ans
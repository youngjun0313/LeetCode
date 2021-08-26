from typing import *
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def rec(l: List[int], p: List[int]):
            if(len(p) == len(nums)):
                ans.append(p)
            else:
                for i in range(len(l)):
                    rec(l[:i] + l[i+1:], p+[l[i]])
        rec(nums, [])
        return ans
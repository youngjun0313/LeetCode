# 오래걸림
from typing import *
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        steps = [0] * n
        for i in range(n):
            for j in range(1, nums[i]+1):
                if(i+j<n and steps[i + j] == 0):
                    steps[i + j] = steps[i] + 1
                else:
                    continue
        return steps[n-1]
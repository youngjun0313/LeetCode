from typing import *
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = nums[0]
        if(len(nums)<2):
            return True
        for i in range(1, len(nums)):
            if(maxJump < i):
                return False
            if(maxJump>=len(nums)-1):
                return True
            if(maxJump<nums[i]+i):
                maxJump = nums[i]+i
        return False
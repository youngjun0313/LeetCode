from typing import *
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        check = False
        index = None
        n = len(nums)
        for i in range(1, n):
            if(nums[i-1] < nums[i]):
                check = True
                index = i
        if(check and index != None):
            temp = nums[index]
            nums[index] = nums[index-1]
            nums[index-1] = temp
        else:
            for i in range(n//2 - 1):
                temp = nums[n-1-i]
                nums[i] = nums[n-1-i]
                nums[n-1-i] = temp
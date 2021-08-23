# 오래 걸림.
from typing import *
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        check = False
        index = None
        n = len(nums)
        for i in range(n-1):
            if(nums[n-i-2]< nums[n-i-1]):
                check = True
                min = nums[n-i-1]
                index = n-i-1
                for j in range(n-i, n):
                    if(nums[j]<min and nums[j]>nums[n-i-2]):
                        min = nums[j]
                        index = j
                nums[index] = nums[n-i-2]
                nums[n-i-2] = min
                for j in range(index, n-1):
                    if(nums[j] < nums[j+1]):
                        temp = nums[j]
                        nums[j] = nums[j+1]
                        nums[j+1] = temp
                for j in range((i-1)//2+1):
                    temp = nums[n-i-1+j]
                    nums[n-i-1+j] = nums[n-1-j]
                    nums[n-j-1] = temp
                break
        
        if(not check):
            for i in range(n//2):
                temp = nums[n-1-i]
                nums[n-1-i] = nums[i]
                nums[i] = temp
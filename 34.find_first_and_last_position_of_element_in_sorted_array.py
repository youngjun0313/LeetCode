from typing import *
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if(not target in nums):
            return [-1,-1]
        def searchPivot(nums: List[int], target: int, start: bool):
            p = 0
            q = len(nums)-1
            if(start):
                while(q-p>1):
                    if(nums[(p+q)//2]<target):
                        p = (p+q)//2
                    else:
                        q = (p+q)//2
                if(nums[p] == target):
                    return p
                else:
                    return q
            else:
                while(q-p>1):
                    if(nums[(p+q)//2]>target):
                        q = (p+q)//2
                    else:
                        p = (p+q)//2
                if(nums[q] == target):
                    return q
                else:
                    return p

        
        return [searchPivot(nums, target, True), searchPivot(nums, target, False)]
from typing import *
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(not target in nums):
            return -1
        n = len(nums)
        p = 0
        q = n-1
        pivot = None
        while(q-p>1):
            if(nums[p] < nums[(p+q)//2]):
                p = (p+q)//2
            else:
                q = (p+q)//2
        if(nums[p]<nums[q]):
            pivot = p
        else:
            pivot = q
        l = nums + nums
        l = l[pivot: n+pivot]
        return (l.index(target)+pivot)%n

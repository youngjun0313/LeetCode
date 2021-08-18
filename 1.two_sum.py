from typing import *

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i] + nums[j] == target):
                return [i, j]

def twoSum2(nums: List[int], target: int) -> List[int]:
    for i in nums:
        if(target - i in nums):
            if(target - i == i):
                if(nums.count(i) == 2):
                    return [nums.index(i), nums.index(i, nums.index(i)+1, len(nums))]
            else:
                return [nums.index(i), nums.index(target-i)]

nums = [2,7,11,15]
target = 9
twoSum(nums, target)
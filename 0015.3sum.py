from typing import *
def threeSum(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    sortedNums = sorted(nums)
    ans = []
    for i in range(n):
        p = i + 1
        q = n - 1
        while(q-p>0):
            if(sortedNums[p]+sortedNums[q]+sortedNums[i] == 0):
                if(not [sortedNums[i],sortedNums[p],sortedNums[q]] in ans):
                    ans.append([sortedNums[i],sortedNums[p],sortedNums[q]])
                p=p+1
            elif(sortedNums[p]+sortedNums[q]+sortedNums[i] < 0):
                p=p+1
            else:
                q=q-1
    return ans
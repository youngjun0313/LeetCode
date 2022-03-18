from typing import *
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if(len(intervals) == 1):
            return [intervals[0]]
        intervals.sort(key=lambda x:(x[0], x[1]))
        start = intervals[0][0]
        end = intervals[0][1]
        ans = []
        for i in range(1, len(intervals)):
            if(intervals[i][0]>end):
                ans.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            elif(intervals[i][1]>end):
                end = intervals[i][1]
                
        ans.append([start, end])

        return ans
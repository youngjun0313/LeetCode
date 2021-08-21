# 오래 걸림.
from typing import *

def maxArea(height: List[int]) -> int:
    n = len(height)
    p = 0
    q = n-1
    shortIndex = p
    shortFront = True
    if(height[q] < height[p]):
        shortIndex = q
        shortFront = False
    maxV = (n-1)*height[shortIndex]
    while(q-p>0):
        if(shortFront):
            p = p + 1
            if((q - p)*min(height[p], height[q]) > maxV):
                maxV = (q - p) * min(height[p], height[q])
            if(height[p] > height[p-1] and height[p]> height[q]):
                shortFront = False
        else:
            q = q - 1
            if((q - p)*min(height[q], height[p]) > maxV):
                maxV = (q - p) * min(height[p], height[q])
            if(height[q] > height[q+1] and height[q]> height[p]):
                shortFront = True
    return maxV
from typing import *
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search_row(mat, target):
            l = [mat[i][0] for i in range(len(mat))]
            h=0
            t=len(l)-1
            if(h == t):
                return h
            pivot = (h+t)//2
            while(t-h>1):
                pivot = (h+t)//2
                if(l[pivot]<=target):
                    h = pivot
                else:
                    t = pivot

            if(target >= l[h+1]):
                return h+1
            else:
                return h
        
        def binary_search_col(l, target):
            h=0
            t=len(l)-1
            if(h == t):
                return l[h]==target
            pivot = (h+t)//2
            while(t-h>1):
                pivot = (h+t)//2
                if(l[pivot]<=target):
                    h = pivot
                else:
                    t = pivot

            if(l[h] == target or l[h+1] == target):
                return True
            else:
                return False

        return binary_search_col(matrix[binary_search_row(matrix, target)], target)
from typing import *
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        map = [[0]*(n+1) for _ in range(m+1)]
        map[1][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                map[i][j] = map[i-1][j]+map[i][j-1] + map[i][j]

        return map[m][n]
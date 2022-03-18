from typing import *
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        map = [[-1]*(n) for _ in range(m)]
        map[0][0] = grid[0][0]
        for i in range(1, n):
            map[0][i] = grid[0][i]+map[0][i-1]

        for j in range(1, m):
            map[j][0] = grid[j][0]+map[j-1][0]

        for i in range(1, m):
            for j in range(1, n):
                if(map[i][j-1]<map[i-1][j]):
                    map[i][j] = grid[i][j] + map[i][j-1]
                else:
                    map[i][j] = grid[i][j] + map[i-1][j]

        return map[m-1][n-1]
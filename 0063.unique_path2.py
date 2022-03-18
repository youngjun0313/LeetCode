from typing import *
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if(obstacleGrid[0][0]):
            return 0
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        map = [[0]*(n+1) for _ in range(m+1)]
        map[1][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if(obstacleGrid[i-1][j-1]==1):
                    continue
                map[i][j] = map[i-1][j]+map[i][j-1] + map[i][j]

        return map[m][n]
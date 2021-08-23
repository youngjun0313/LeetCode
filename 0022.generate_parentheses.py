from typing import *
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def rec(openCount: int, closeCount: int, s: str):
            if(openCount == 0 and closeCount == 0):
                ans.append(s)
            elif(openCount == 0):
                rec(openCount, closeCount-1, s + ')')
            else:
                rec(openCount-1, closeCount, s + '(')
                if(openCount < closeCount):
                    rec(openCount, closeCount-1, s + ')')
        rec(n, n, '')
        return ans
    
s = Solution()
print(s.generateParenthesis(3))
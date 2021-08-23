from typing import *
from typing_extensions import IntVar
def letterCombinations(digits: str) -> List[str]:
    alphas= [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
    ans = []
    digitList = list(digits)
    digitListInt = list(map(int, digitList))
    def minus2(n: int):
        return n-2

    def rec(l: List[int], s: str):
        if(len(l) == 0):
            return
        if(len(l) == 1):
            if(l[0] == 5 or l[0] == 7):
                for i in range(4):
                    ans.append(s + alphas[l[0]][i])
            else:
                for i in range(3):
                    ans.append(s + alphas[l[0]][i])
        else:
            if(l[0] == 5 or l[0] == 7):
                for i in range(4):
                    rec(l[1:], s + alphas[l[0]][i])
                return
            else:
                for i in range(3):
                    rec(l[1:], s + alphas[l[0]][i])
                return
    rec(list(map(minus2, digitListInt)), "")
    return ans

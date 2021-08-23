# 오래 걸림.
from os import PathLike


def longestPalindrome(s: str) -> str:
    if(s == ""):
        return s
    n = len(s)
    palinStart = 0
    palinEnd = 0
    palinArray = [[False]*n for _ in range(n)]

    for k in range(n):
        for i in range(n-k):
            j = i + k
            if(k==0):
                palinArray[i][j] = True
                palinStart = i
                palinEnd = j
            elif(k == 1 or k == 2):
                if(s[i] == s[j]):
                    palinArray[i][j] = True
                    palinStart = i
                    palinEnd = j
            else:
                if(palinArray[i+1][j-1] and s[i] == s[j]):
                    palinArray[i][j] = True
                    palinStart = i
                    palinEnd = j

    return s[palinStart: palinEnd+1]
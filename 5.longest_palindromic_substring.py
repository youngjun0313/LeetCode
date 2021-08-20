# 오래 걸림.
from os import PathLike


def longestPalindrome(s: str) -> str:
    if(s == ""):
        return s
    palinArray = []
    palinStart = 0
    palinEnd = 0
    for k in range(len(s)):
        palinArray.append([])
        for i in range(len(s)-k):
            palinArray[k].append(False)

    for k in range(len(s)):
        for i in range(len(s)-k):
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
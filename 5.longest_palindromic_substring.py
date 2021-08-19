def longestPalindrome(s: str) -> str:
    if(s == ""):
        return 0
    if(len(s) == 1):
        return 1
    maxLen = 0
    temp = ""
    ans = ""
    for i in range(len(s)):
        temp = temp + s[i]
        subTemp = temp[temp.index(s[i]) : ]
        revSubTemp = ''.join(reversed(subTemp))
        if(temp.index(s[i]) != len(temp)-1 and subTemp == revSubTemp):
            if(len(subTemp) > maxLen):
                maxLen = len(subTemp)
                ans = subTemp
    return ans

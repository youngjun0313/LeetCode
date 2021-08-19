def lengthOfLongestSubstring(s: str) -> int:
    if(s == ""):
        return 0
    else:
        maxLen = 0
        tempList = []
        for i in range(len(s)):
            if(not s[i] in tempList):
                tempList.append(s[i])
                if(len(tempList) > maxLen):
                    maxLen = len(tempList)
            else:
                tempList.append(s[i])
                tempList = tempList[tempList.index(s[i])+1:]
        return maxLen

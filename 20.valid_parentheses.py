class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        sList = list(s)
        pList = []
        for i in range(n):
            if(sList[i] == '(' or sList[i] == '{' or sList[i] == '['):
                pList.append(sList[i])
            elif(pList != []):
                if(sList[i] == ')'):
                    temp = pList.pop()
                    if(temp == '('):
                        pass
                    else:
                        return False
                elif(sList[i] == '}'):
                    temp = pList.pop()
                    if(temp == '{'):
                        pass
                    else:
                        return False
                elif(sList[i] == ']'):
                    temp = pList.pop()
                    if(temp == '['):
                        pass
                    else:
                        return False
            else:
                return False
        if(pList == []):
            return True
        else:
            return False
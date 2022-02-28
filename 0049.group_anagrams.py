from typing import *
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i in range(len(strs)):
            str = "".join(sorted(strs[i]))
            if(ans.get(str, -1) == -1):
                ans[str] = [strs[i]]
            else:
                ans[str].append(strs[i])
                
        return ans.values()

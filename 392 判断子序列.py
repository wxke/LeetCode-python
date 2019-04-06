判断子序列
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        flag = 0
        for i in s:
            try:
                ind = t.index(i)
                t = t[ind+1:]

            except:
                return False
            # print(ind)
            # print(t)
        
        return True

检查替换后的词是否有效
class Solution:
    def isValid(self, S: str) -> bool:
        while "abc" in S:
            S = S.replace("abc","")
        
        return S == ""

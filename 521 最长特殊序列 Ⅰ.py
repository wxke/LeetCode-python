最长特殊序列 Ⅰ
class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        else:
            if len(a)>len(b):
                return len(a)
            else:
                return len(b)
        

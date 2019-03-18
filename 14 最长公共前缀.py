最长公共前缀
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs:
            strs.sort(key=len)
            a = strs[0]
            len1 = len(a)
            for i in strs:
                if a[:len1] == i[:len1]:
                    continue
                else:
                    while True:
                        len1 -= 1
                        if a[:len1] in i[:len1] :
                            break
                        if len1 ==0:
                            return ""
            return a[:len1]
        else:
            return ""
        
                        
        
            
            

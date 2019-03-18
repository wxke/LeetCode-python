实现strStr()
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        else:
            try:
                return haystack.index(needle)
            except:
                return -1
        

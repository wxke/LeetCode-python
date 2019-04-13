重复的子字符串
class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        len1 = len(s)
        j = 1
        for  i in range(len(s)//2):
            a = s
            old = s[:i+1]
            if old * (len1 // j) == s:
                return True
            j = j +1
        return False

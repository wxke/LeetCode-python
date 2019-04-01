有效的字母异位词
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in t:
                t = t.replace(s[i],"",1)
            else:
                return False
        if len(t):
            return False
        else:
            return True


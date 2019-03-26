验证回文串
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        num = ""
        for i in s:
            if i.isalnum():
                num +=i
        return num == num[::-1]

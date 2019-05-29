最短回文串
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        for i in range(n - 1, -1, -1):
            if s[0:i+1] == s[i::-1]:
                return s[-1:i:-1] + s
        return ""
        

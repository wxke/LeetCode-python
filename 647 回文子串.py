回文子串
class Solution:
    def countSubstrings(self, s: str) -> int:
        cont = 0
        def dp(s,left,right,ans):
            while left >=0 and right < len(s) and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
            return ans
        for i in range(len(s)):
            cont += dp(s,i,i,0)
            cont += dp(s,i,i+1,0)

        return cont

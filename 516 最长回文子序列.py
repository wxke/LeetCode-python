最长回文子序列
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for j in range(n)] for i in range(n)]

        dp[0][0] = 1
        for i in range(n):
            dp[i][i] = 1
            for j in range(i-1,-1,-1):
                if s[i] == s[j]:
                    dp[j][i] = dp[j+1][i-1] + 2
                else:
                    dp[j][i] = max(dp[j+1][i],dp[j][i-1])


        return dp[0][n-1]  
        
#         def dp(s,res):
#             if len(s) == 0:
#                 return 0
#             elif len(s) == 1:
#                 return 1
#             elif len(s) == 2 and s[0] == s[-1]:
#                 return 2
#             for i in range(len(s)):
#                 if s[0] == s[-1]:
#                     res += dp(s[1:-1],res) + 2
#                 else:
#                     res += max(dp(s[0:-1],res),dp(s[1:],res))
                
#                 return res
#         return dp(s,0)
         

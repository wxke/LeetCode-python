两个字符串的最小ASCII删除和
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + ord(s1[i - 1])
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return (sum(ord(q) for q in s1) + sum(ord(q) for q in s2) - dp[-1][-1]* 2 )

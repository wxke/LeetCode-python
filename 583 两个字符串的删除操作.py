两个字符串的删除操作
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        for i in range(len(word1)):
            for j in range(len(word2)):
                # print(dp)
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    # print(i,j)
                    dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
            
        return len(word1) - dp[-1][-1] + len(word2) - dp[-1][-1]

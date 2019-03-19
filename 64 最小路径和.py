最小路径和
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[0 for i in range(len(grid[0]))] for j in range(len(grid)) ]
        cont = 0 
        for i in range(len(grid[0])):
            dp[0][i] = cont+grid[0][i]
            cont +=grid[0][i]
        for i in range(1,len(grid)):
            for j in range(len(grid[0])):
                if j == 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j],dp[i][j-1])
        # print(dp)
        return dp[-1][-1]

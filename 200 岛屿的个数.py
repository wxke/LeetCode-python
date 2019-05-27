岛屿的个数
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dp(i,j):
            grid[i][j] = '0'
            if i - 1 >= 0 and grid[i-1][j] == '1':
                dp(i-1,j)
            if i + 1 < len(grid) and grid[i+1][j] == '1':
                dp(i+1,j)
            if j - 1 >= 0 and grid[i][j-1] == '1':
                   dp(i,j-1)
            if j + 1 < len(grid[0]) and grid[i][j+1] == '1':
                   dp(i,j+1)
        
        
        if grid == []:
            return 0
        r = len(grid)
        c = len(grid[0])
        sum1 = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    sum1 += 1
                    dp(i,j)
        return sum1
        

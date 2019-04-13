岛屿的周长
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum = 0
        recount = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    sum += 1
                    if i-1>=0:
                        if grid[i-1][j] == 1:
                            recount +=1
                    if j -1 >= 0:
                        if grid[i][j-1] == 1:
                            recount +=1
                    if i +1 <n:
                        if grid[i+1][j]:
                            recount +=1
                    if j+1 <m:
                        if grid[i][j+1]:
                            recount +=1
                            
        return sum *4 -recount



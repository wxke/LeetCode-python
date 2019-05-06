三维形体的表面积
class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sumArea = 0
        for i in grid:
            for j in i:
                if j ==0:
                    sumArea +=0
                elif j ==1:
                    sumArea +=6
                elif j == 2:
                    sumArea +=10
                else:
                    sumArea += 10 + (j-2) * 4

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i - 1 >=0:
                    sumArea -=min(grid[i][j],grid[i-1][j])
                if i + 1 < len(grid):
                    sumArea -= min(grid[i+1][j],grid[i][j])
                if j -1 >=0:
                    sumArea -= min(grid[i][j],grid[i][j-1])
                if j +1 <len(grid):
                    sumArea -= min(grid[i][j+1],grid[i][j])



        return sumArea

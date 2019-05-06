三维形体投影面积
class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum1 = 0
        list_hang = []
        list_lie = []
        for i in range(len(grid)):
            list_hang.append(max(grid[i]))
        big = 0
        for i in range(len(grid[0])):
            big = 0
            for j in range(len(grid)):
                if big <grid[j][i]:
                    big = grid[j][i]
            list_lie.append(big)
            
        sum1 = sum1 +sum(list_hang) +sum(list_lie)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] !=0:
                    sum1 += 1
                
        return sum1
        
        

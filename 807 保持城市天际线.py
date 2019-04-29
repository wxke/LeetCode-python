保持城市天际线
class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = []
        for i in grid:
            h.append(max(i))
        l = []
        for i in range(len(grid[0])):
            list1 = []
            for j in range(len(grid)):
                list1.append(grid[j][i])
            l.append(max(list1))
        cont = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cont += min(l[j],h[i]) - grid[i][j]
        return cont

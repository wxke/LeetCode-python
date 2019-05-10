由斜杠划分区域
class Solution:
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        q = [[0 for j in range(len(grid[0])*4)] for i in range(len(grid)*4)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if  grid[i][j] == '\\':
                    q[4*i][4*j] = 1
                    q[4 * i +1][4 * j+1] =1
                    q[4 * i + 2][4 * j + 2] = 1
                    q[4 * i + 3][4 * j + 3] = 1
                if grid[i][j] == '/':
                    q[4 * i ][4 * j +3] = 1
                    q[4 * i+1][4 * j+2] = 1
                    q[4 * i+2][4 * j+1] = 1
                    q[4 * i+3][4 * j+0] = 1
        cont = 0
        def dp(i,j):
            if i + 1 <len(q) and q[i+1][j] == 0:
                q[i+1][j] = 1
                dp(i+1,j)
            if i - 1 >=0 and q[i-1][j] == 0:
                q[i-1][j] = 1
                dp(i-1,j)
            if j+1 <len(q) and q[i][j+1] == 0:
                q[i][j+1] = 1
                dp(i,j+1)
            if j-1 >=0 and q[i][j-1] == 0:
                q[i][j-1] = 1
                dp(i,j-1)
        for i in range(len(q)):
            for j in range(len(q[0])):
                if q[i][j] == 0:
                    dp(i,j)
                    cont +=1

        return cont


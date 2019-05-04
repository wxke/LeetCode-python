矩阵中的幻方
class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cont = 0
        list1 = [i for i in range(1,10)]
        if len(grid) <3 or len(grid[0]) <3:
            return cont
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                list2 = [grid[i][j],grid[i][j+1],grid[i][j+2],
                         grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2],
                         grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]]
                list2 = sorted(list2)
                if list2 == list1:
                    sum1 = grid[i][j]+grid[i][j+1]+grid[i][j+2]
                    sum2 = grid[i+1][j]+grid[i+1][j+1]+grid[i+1][j+2]
                    sum3 = grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2]
                    sum4 = grid[i][j]+grid[i+1][j]+grid[i+2][j]
                    sum5 = grid[i][j+1]+grid[i+1][j+1]+grid[i+2][j+1]
                    sum6 = grid[i][j+2]+grid[i+1][j+2]+grid[i+2][j+2]
                    sum7 = grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]
                    sum8 = grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2]
                    # print(sum1 == sum2 == sum3 == sum4 == sum5 == sum6 == sum7 == sum8)
                    # print(sum1 , sum2 , sum3 , sum4 , sum5 , sum6 , sum7 , sum8)
                    if sum1 == sum2 == sum3 == sum4 == sum5 == sum6 == sum7 == sum8:
                        cont += 1
                
        return cont 

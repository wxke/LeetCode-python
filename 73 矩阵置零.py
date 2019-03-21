矩阵置零
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = []
        c = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    r.append(i)
                    c.append(j)
        
        for i in r:
            matrix[i] = [0 for i in range(len(matrix[0]))]
        
        for j in c:
            for i in range(len(matrix)):
                matrix[i][j] = 0
                

        
        

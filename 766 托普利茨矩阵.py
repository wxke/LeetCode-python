托普利茨矩阵
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        flag = True
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                try:
                    if matrix[i][j] != matrix[i+1][j+1]:
                        flag = False
                except:
                    continue
                    
        return flag
                    

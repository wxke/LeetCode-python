旋转图像
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
        hang = len(matrix)
        lie = len(matrix[0])
        flag = lie - 1
        i = 0
        while i < hang * lie:
            if flag == i%lie:
                i += lie-flag
                flag -= 1
                if flag == 0:
                    break
                continue
            matrix[i//hang][i%lie],matrix[hang-i%lie-1][lie-i//hang-1] = matrix[hang-i%lie-1][lie-i//hang-1]
                ,matrix[i//hang][i%lie]
            i = i+1
            
#        5 1 9 11     11 9 1 5
#        2 4 8 10     10 8 4 2
#        13 3 6 7     6 7 3 13
#        15 14 12 16  16 12 14 15
                    
# 15 13 1 5            15 13 2 5
# 14 3 4 2             14 3 4 1
# 7 6 8 9              12 6 8 9
# 16 12 10 11          16 7 10 11
            

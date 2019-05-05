转置矩阵
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        list = [ []for i in range(len(A[0]))]
        q =0
        for i in range(len(A[0])):
            for j in range(len(A)):
                list[q].append(A[j][i])
            q = q +1

        return list
            
        

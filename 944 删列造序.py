删列造序
class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        sum1 = 0
        for i in range(len(A[0])):
            s = []
            for j in range(len(A)):
                s.append(A[j][i])
            
            if s == sorted(s) :
                sum1 +=1
                
        
        return len(A[0]) - sum1
        

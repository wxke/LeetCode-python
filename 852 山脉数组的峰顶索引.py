山脉数组的峰顶索引
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        flag = A[0]
        for i in range(1,len(A)):
            if A[i]>flag:
                flag = A[i]
            else:
                flag = i-1
                break
        
        return flag
                
            

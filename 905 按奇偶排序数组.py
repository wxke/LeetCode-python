按奇偶排序数组
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        list = []
        for i in range(len(A)):
            if A[i] % 2 ==0:
                list.append(A[i])
                A[i]  = -1
        
        for i  in A:
            if i !=-1:
                list.append(i)
                
        return list
                

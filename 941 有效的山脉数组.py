有效的山脉数组
class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A)>2:
            if A == sorted(A) or A[::-1] == sorted(A):
                return False
            max1 = max(A)
            lin = A.index(max1)
            for i in range(1,lin):
                if A[i-1] >= A[i]:
                    return False
            for i in range(lin+1,len(A)):
                if A[i-1] <= A[i]:
                    return False
        else:
            return False
        return True
        

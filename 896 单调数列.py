单调数列
class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        B = sorted(A)
        if A == B or A == B[::-1]:
            return True
        else:
            return False
        

最小差值 I
class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if min(A) + K >= max(A)-K:
            return 0
        else:
            return max(A) - min(A) -K - K
        

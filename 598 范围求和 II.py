范围求和 II
class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        for i in ops:
            m = min(i[0],m)
            n = min(i[1],n)



        return m*n

组合
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # list1 = [i for i in range(1,n+1)]
        return list(itertools.combinations(range(1,n+1),k))

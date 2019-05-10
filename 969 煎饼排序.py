煎饼排序
class Solution:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
     # 3   4 2 3 1
     # 4   1 3 2 4
     # 2   3 1 2 4
     # 3   2 1 3 4
     # 2   1 2 3 4   
        q = sorted(A,reverse=True)
        res = []
        len1 = len(q)
        for i,j in enumerate(q):
            ind = A.index(j)+1
            res.append(ind)
            res.append(len1-i)
            A = A[:ind][::-1]+A[ind:]
            A = A[:len1-i][::-1] + A[len1-i:]
        return res

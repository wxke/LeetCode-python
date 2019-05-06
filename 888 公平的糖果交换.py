公平的糖果交换
class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum_A  = sum(A)
        sum_B  = sum(B)
        sum_1 = (sum_A - sum_B) // 2
        A = list(set(A))
        B = set(B)
        for i in range(len(A)):
            if A[i] - sum_1 in B:
                return [A[i],A[i] - sum_1]

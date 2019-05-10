重复 N 次的元素
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        A = sorted(A)
        
        import collections
        A = collections.Counter(A)
        N = len(A) -1

        for k,v in A.items():
            if v == N:
                return k
            

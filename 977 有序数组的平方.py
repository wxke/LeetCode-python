有序数组的平方
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
         A = [i**2 for i in A]
         return sorted(A)
        
        

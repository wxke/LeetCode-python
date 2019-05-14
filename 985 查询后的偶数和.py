查询后的偶数和
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        res =[]
        sum1 = sum(i for i in A if i%2==0)
        


        for i in queries:
            if A[i[1]] % 2 == 0:
                sum1 -= A[i[1]]
            A[i[1]] += i[0]
            if A[i[1]] % 2 == 0:
                sum1 += A[i[1]]
            res.append(sum1)
  
            
        return res

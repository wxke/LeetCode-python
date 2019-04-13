四数相加 II
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        res = []
        for i in A:
            for j in B:
                res.append(i+j)
        ans = {}
        for i in C:
            for j in D:
                if i + j in ans:
                    ans[i+j] += 1
                else:
                    ans[i+j] = 1
        cout = 0 
        for i in res:
            if 0 - i in ans:
                 cout += ans[-i]
        
        return cout

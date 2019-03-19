组合总和 II
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dp(a,sum1,target):
            if sum1 == target:
                res.append(a[::])
                return
            for v,i in enumerate(candidates):
                if sum1 +i > target:
                    continue
                a.append(i)
                candidates.pop(v)
                dp(a,sum1+i,target)
                candidates.insert(v,i)
                a.pop()
        dp([],0,target)
        a = []
        for i in res:
            q = sorted(i)
            if q in a:
                continue
            else:
                a.append(sorted(i))
        return a

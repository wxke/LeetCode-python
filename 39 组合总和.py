组合总和
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dp(a,sum1,target):
            if sum1 == target:
                res.append(a[::])
                return
            for i in candidates:
                if sum1 +i > target:
                    continue
                a.append(i)
                dp(a,sum1+i,target)
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

组合总和 III
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        s = []
        if n // k >=9:
            return []

        def dp(a, k,q):
            if k == 0 and q == n:
                s.append(a[::])
                return
            elif  k == 0:
                return
            for i in range(1, 10):
                if i not in a:
                    a.append(i)
                    dp(a, k - 1,q+i)
                    a.pop()

        dp([], k,0)
        a = []
        for i in s:
            i = sorted(i)
            if i not in a:
                a.append(sorted(i))


        return a

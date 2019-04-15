优美的排列
class Solution:
    def countArrangement(self, N: int) -> int:
        q = []
        a = [ i for i in range(1,N+1)]
        def dp(j):
            ans = 0
            if  j== N:
                ans += 1
                return ans

            for i in range(0,N):
                if a[i] != 0 and (a[i] % (j+1) == 0 or (j+1) % a[i] ==0 ):
                    x = a[i]
                    a[i] = 0
                    ans  += dp(j+1)
                    a[i] = x

            return ans
        ans = dp(0)
        return ans

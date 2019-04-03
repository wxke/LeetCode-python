完全平方数
class Solution:
    def numSquares(self, n: int) -> int:
        m = [0 for i in range(n+1)]
        m[0] = 0
        m[1] = 1
        for i in range(2,n+1):
            tmp = sys.maxsize
            j = 1
            while j * j <= i:
                tmp = min(tmp,m[i - j*j])
                j += 1
            m[i] = tmp + 1

        return m[n]

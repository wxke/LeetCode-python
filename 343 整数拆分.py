整数拆分
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return  1
        if n == 3:
            return 2
        sum1 = 1
        while n > 4:
            sum1 *= 3
            n -= 3
        return sum1 * n

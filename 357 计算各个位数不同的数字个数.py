计算各个位数不同的数字个数
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1;
        dp = [1,10,91]
        if n == 1:
            return dp[1]
        elif n == 2:
            return dp[2]
        for i in range(3,n+1):
            dp.append(dp[i-1] + (dp[i-1] - dp[i-2]) *(11 - i))
        
        return dp[-1]

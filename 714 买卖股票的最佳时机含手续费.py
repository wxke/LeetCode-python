买卖股票的最佳时机含手续费
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sum1 = 0
        min1 = prices[0]
        for i in range(1,len(prices)):
            if prices[i] - min1 > fee:

                sum1 += prices[i] - min1 -fee
                min1 = prices[i] -fee
            else:
                min1 = min(min1,prices[i])
        
        return sum1

买卖股票的最佳时机
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min1 = 10000000000
        max1 = 0
        for i in range(len(prices)):
            if min1 > prices[i]:
                min1= prices[i]
            elif prices[i] - min1 >max1:
                max1 = prices[i] - min1
                
        return max1
                

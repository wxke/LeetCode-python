买卖股票的最佳时机 II
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max1 = 0
        for i in range(1,len(prices)):
            if prices[i] >prices[i-1]:
                max1 = max1 + prices[i] - prices[i-1]
        return max1
                

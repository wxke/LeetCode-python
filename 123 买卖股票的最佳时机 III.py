买卖股票的最佳时机 III
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        maxmon = 0
        minprice = 1000000000
        first = []
        last = []
        for i in range(len(prices)):
            minprice = min(minprice, prices[i])
            maxmon = max(maxmon, prices[i] - minprice)
            first.append(maxmon)

        maxmon = 0
        maxprice = prices[-1]
        for i in range(len(prices)-1, -1, -1):
            maxprice = max(maxprice, prices[i])
            maxmon = max(maxmon, maxprice - prices[i])
            last.insert(0, maxmon)

        maxmon = 0
        for i in range(len(prices)):
            maxmon = max(maxmon, last[i] + first[i])
        return maxmon

        
                        
                
        

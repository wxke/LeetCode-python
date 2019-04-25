使用最小花费爬楼梯
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        last , now = cost[0], cost[1]
        for i in range(2,len(cost)):

            last,now = now,min(last+cost[i],now+cost[i])
        return min(last,now)

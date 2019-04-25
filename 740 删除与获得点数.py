删除与获得点数
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        maxNum = max(nums) + 1
        dp = [0] * maxNum
        
        for i in nums:
            dp[i] += 1
        # print(dp)
        for j in range(2,maxNum):
            if dp[j] != 0:
                dp[j] = max(dp[j-1],dp[j-2]+dp[j]*j)
            else:
                dp[j] = dp[j-1]
            
#             print(dp)
        
        
        return dp[-1]
            
            

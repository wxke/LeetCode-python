预测赢家
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def dp(nums,i,j):
            if i == j :
                return nums[i]
            x = nums[i] - dp(nums,i+1,j)
            y = nums[j] - dp(nums,i,j-1)
            return max(x,y)
        
        if len(nums) % 2 == 0 or len(nums) == 1:
            return True
        return True if dp(nums,0,len(nums)-1) > 0 else False

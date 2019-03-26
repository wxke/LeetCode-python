打家劫舍 II
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        
        res1 = [nums[0],max(nums[0],nums[1])]
        
        for i in range(2,n - 1):
            res1.append(max(res1[i-2]+nums[i],res1[i-1]))
            
        
        res2 = [0,nums[1]]
        
        for i in range(2,n):
            res2.append(max(res2[i-2]+nums[i],res2[i-1]))
            
        return max(res2.pop(),res1.pop())

最大连续1的个数
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = 0
        sum1 = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                sum1 +=1
            elif nums[i]==0:
                if sum1 > max1:
                    max1 = sum1
                sum1 = 0
                    
        if sum1 > max1:
                 max1 = sum1
        
        return max1

只出现一次的数字
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = nums[0]
        for i in range(1,len(nums)):
            num = num ^nums[i]
            
        return num
        
        

求众数
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = 1
        nums = sorted(nums)    
        len1 = len(nums)//2
        len1 = len1 +1
        flag = nums[0]
        for i in range(1,len(nums)):
            if flag == nums[i]:
                sum1 +=1
                if sum1 >= len1:
                    break
            else:
                sum1 = 1
                flag = nums[i]
                
        return flag

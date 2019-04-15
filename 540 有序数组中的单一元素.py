有序数组中的单一元素
class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         q = set(nums)
#         for i in q:
#             if nums.count(i) == 1:
#                 return i 
            
        i = 0
        while i <len(nums)-1:
            if nums[i]==nums[i+1]:
                i = i+2
            else:
                return nums[i]
        return nums[-1]

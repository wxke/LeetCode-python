两数之和
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            j = target -nums[i]
            if j in nums[i+1:]:
                return [i,nums[i+1:].index(j)+i+1]

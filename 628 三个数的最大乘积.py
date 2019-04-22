三个数的最大乘积
class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        max1 = nums[-1] * nums[-2] * nums[-3]
        if nums[0]<0 and nums[1] <0:
            max1 = max(max1,nums[0]*nums[1]*nums[-1])
        return max1

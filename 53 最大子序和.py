最大子序和
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        max_sub_sum = nums[0]
        for num in nums:
            sum += num
            if sum > max_sub_sum:
                max_sub_sum = sum
            if sum < 0:
                sum = 0
        return max_sub_sum

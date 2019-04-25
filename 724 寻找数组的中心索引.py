寻找数组的中心索引
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <=2:
            return -1
        left = 0
        right = sum(nums)-nums[0]
        for i in range(1,len(nums)):
            # print(left,right)
            if left == right:
                return i-1
            left += nums[i-1]
            right -= nums[i]
        if left == right:
            return i
        return -1

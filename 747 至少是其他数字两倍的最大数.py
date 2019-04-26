至少是其他数字两倍的最大数
class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        num = sorted(nums)
        max1 = num[-1]
        num= num[:-1]
        if (max1 >= num[-1]*2):
            return nums.index(max1)
        else:
            return -1

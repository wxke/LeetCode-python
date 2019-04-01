寻找重复数
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in set(nums):
            if nums.count(i) >1:
                return i

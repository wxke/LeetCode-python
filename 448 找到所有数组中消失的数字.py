找到所有数组中消失的数字
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set(i for i in range(1,len(nums)+1)) - set(nums))

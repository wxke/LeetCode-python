移除元素
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = nums.count(val)
        for i in range(n):
            nums.remove(val)
                
        return len(nums)

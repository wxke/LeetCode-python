删除排序数组中的重复项
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = ''
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                flag = nums[i]
                nums[i] = 'a'
            if nums[i-1] == 'a' and nums[i] == flag:
                nums[i] = 'a'
        cont = 0
        i = 0
        len1 = len(nums)
        while i < len1:
            if nums[i] == 'a':
                nums.pop(i)
                len1 -= 1
            else:
                i = i + 1

        return len(nums[:i])

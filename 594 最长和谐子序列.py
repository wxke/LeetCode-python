最长和谐子序列
class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            dic_nums = collections.Counter(nums)
            flag = nums[0]
            max1 = 0
            nums =sorted(nums)
            for i in range(1,len(nums)):
                if nums[i] - flag == 1:
                    max1 = max(max1,dic_nums[flag]+dic_nums[nums[i]])
                flag = nums[i]
            return max1
        else:
            return 0

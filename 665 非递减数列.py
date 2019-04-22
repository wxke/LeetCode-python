非递减数列
class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1] :
                count += 1
                if i - 2 < 0 or nums[i-2] < nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
            if count > 1:
                return False
        return True

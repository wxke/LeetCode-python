最短无序连续子数组
class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums1 = sorted(nums)
        if nums1 == nums:
            return 0
        for i in range(len(nums)):
            if nums[i] != nums1[i]:
                break
        for j in range(len(nums)-1,0,-1):
            # print(nums[j])
            if nums[j] != nums1[j]:
                break
        return j - i + 1

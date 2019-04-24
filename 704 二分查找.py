二分查找
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import bisect
        inde = bisect.bisect_left(nums,target)
        if inde>=len(nums) or nums[inde] != target:
            return -1
        else:
            return inde
        

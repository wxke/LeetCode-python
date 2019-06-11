数组中的K-diff数对
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        import bisect
        nums = sorted(list(nums))
        res = []
        len1 = len(nums)
        for j,i in enumerate(nums):
            q = bisect.bisect_left(nums,k+i)
            if q<len1 and nums[q] == k+i and j != q:
                res.append((i,nums[q]))
        
        return len(set(res))

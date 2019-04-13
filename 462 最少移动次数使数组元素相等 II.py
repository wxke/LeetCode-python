最少移动次数使数组元素相等 II
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        res = 0
        while i < j :
            res += nums[j] - nums[i]
            i += 1
            j -= 1
        
        return res

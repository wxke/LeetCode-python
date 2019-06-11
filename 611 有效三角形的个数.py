有效三角形的个数
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        len1 = len(nums)
        res = 0
        import bisect
        for i in range(len1-2):
            for j in range(i+1,len1-1):
                x = nums[i] + nums[j] - 1
                index = bisect.bisect_right(nums[j+1:],x)

                res += index 

        
        return res
        

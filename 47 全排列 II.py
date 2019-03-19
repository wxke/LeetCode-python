全排列 II
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dp(nums,a):
            if nums == []:
                res.append(a[::])
                return
            for i in range(len(nums)):
                a.append(nums[i])
                dp(nums[:i]+nums[i+1:],a)
                a.pop()
        dp(nums,[])
        ans = []
        for i in res:
            if i not in ans:
                ans.append(i)
        return ans


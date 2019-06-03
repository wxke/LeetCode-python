递增子序列
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        len1 = len(nums)
        def dfs(nums,a):
            if len(a) >=2:
                res.add(tuple(a[::]))
            for j in range(len(nums)):
                if nums[j] >= a[-1]:
                    a.append(nums[j])
                    dfs(nums[j+1:],a)
                    a.pop()
        for i in range(len1):
            dfs(nums[i+1:],[nums[i]])

        return list(res)

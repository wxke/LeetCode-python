颜色分类
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = []
        j = 0
        for i in nums:
            if i == 0:
                res.insert(0,0)
                j+=1
            if i == 1:
                res.insert(j,1)
            if i == 2:
                res.append(2)

        
        for i in range(len(nums)):
            nums[i] = res[i]
        

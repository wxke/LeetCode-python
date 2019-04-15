最优除法
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1]) 
        str1 ="" + str(nums[0]) + "/("
        for i in nums[1:]:
            str1 += str(i) + '/'
        
        str1 = str1[:-1]
        str1 += ")"
        return str1

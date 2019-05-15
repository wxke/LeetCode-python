删除排序数组中的重复项 II
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        flag = nums[0]
        sum1 = 0
        sum2 = 0
        len1 = len(nums)
        for i in range(0,len1):
            if flag == nums[i]:
                sum1 += 1
            else:
                flag = nums[i] 
                sum1 = 1
            if sum1 >2 :
                nums[i] = 'a'
                sum1 -= 1
                sum2 += 1
        
        for i in range(0,len1):
            if nums[i] =='a' :
                j = i
                while j < len1-1 and nums[j] == 'a':
                    j += 1
                
                nums[i],nums[j] = nums[j],nums[i]
                
        return len1 - sum2
        
        
            
            
        

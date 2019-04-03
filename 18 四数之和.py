四数之和
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        len1 = len(nums)
        res = [] 
        for i in range(len1):
            x = nums[i]
            nums[i] = 'q'
            for j in range(i+1,len1):
                y = nums[j]
                nums[j] = 'q'
                for q in range(j+1,len1):
                    n = nums[q]
                    nums[q] = 'q'
                    sum1 = target - x - y - n
                    if sum1 in nums:
                        res.append([x,y,n,sum1])
                    nums[q] = n
                nums[j] = y
            nums[i] = x
        
        ans = []
        for i in res:
            i.sort()
            if i not in ans:
                ans.append(i)
                    
        return ans                   

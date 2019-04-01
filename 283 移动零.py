移动零
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n=nums.count(0)
        for i in range(n):
            nums.remove(0)
        for i in range(n):
            nums.append(0) 
        
                
        

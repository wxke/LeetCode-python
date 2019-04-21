重塑矩阵
class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r*c:
            return nums
        else:
            list =[]
            for i in range(len(nums)):
                for j in range(len(nums[0])):
                    list.append(nums[i][j])
            
            nums = [[0 for i in range(c)] for j in range(r)]
            for i in range(r):
                for j in range(c):
                    nums[i][j] = list[i*c+j]
                
            return nums
            
            

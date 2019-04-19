数组拆分 I
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        list =[]
        list.extend(nums)
        list.sort()
        sum = 0
        for i in range(0,len(list),2):

            sum = sum + list[i]
        return sum
        

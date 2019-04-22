子数组最大平均数 I
class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        cont = sum(nums[:k])
        list1 = [cont]
        for i in range(len(nums) - k ):
            a = cont-nums[i]+nums[i+k]
            list1.append(a)
            cont = a     
        return max(list1) / k 

到最近的人的最大距离
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        nums = []
        for i in range(len(seats)):
            if seats[i] == 1:
                nums.append(i)
        max1 = 0
        len1 = len(nums)
        for i in range(1,len1):
            max1 = max(max1,(nums[i] - nums[i-1]) // 2)
        
        
        return max(nums[0], len(seats) - nums[-1] -1,max1)
                

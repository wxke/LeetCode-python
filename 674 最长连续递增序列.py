最长连续递增序列
class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            max1 = 0
            flag = nums[0]
            cont = 1
            for i in nums[1:]:
                if flag < i:
                    cont +=1
                else:
                    max1 = max(max1,cont)
                    cont = 1
                flag = i
            max1 = max(max1, cont)
            return max1
        else:
            return 0

数组中重复的数据
class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list1 = [0 for i in range(len(nums)+1)]
        for i in nums:
            list1[i] +=1
        q = []
        for i in range(len(list1)):
            if list1[i] == 2:
                q.append(i)
        return q
                                  

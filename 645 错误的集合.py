错误的集合
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        max1 = max(nums)
        nums = collections.Counter(nums)
        nums = dict(nums)
        list1 = []
        for i,j in nums.items():
            if j == 2:
                list1.append(i)
                break
        flag = 1
        for i in range(max1):
            try:
                nums[i+1]
            except:
                list1.append(i+1)
                flag = 0
                break
        if flag:
            list1.append(max1+1)
            return list1
        return list1

        

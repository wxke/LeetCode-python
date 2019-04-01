除自身以外数组的乘积
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums.count(0) > 1:
            return [0 for i in range(len(nums))]
        a = 1
        q = 1
        for i in nums:
            a = a* i 
            if i == 0:
                continue
            q = q * i
        li = []
        for i in nums:
            if i != 0:
                li.append(a//i)
            else:
                li.append(q)
        return li

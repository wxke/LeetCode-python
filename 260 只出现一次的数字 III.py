只出现一次的数字 III
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = dict(collections.Counter(nums))
        res = []
        a = 0
        for k,v in n.items():
            if v == 1:
                res.append(k)
                a = a+1
            if a == 2:
                return res
            

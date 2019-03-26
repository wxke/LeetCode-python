只出现一次的数字 II
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = dict(collections.Counter(nums))
        for k,v in n.items():
            if v == 1:
                return k
        

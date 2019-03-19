全排列
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # a = list(itertools.permutations(nums,len(nums)))
        # list1 = []
        # for i in a:
        #     list1.append(list(i))
        return list(itertools.permutations(nums,len(nums)))

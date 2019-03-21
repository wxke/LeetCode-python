子集
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        list2 = []
        for i in range(len(nums)+1):
            list1 = list(itertools.combinations(nums, i))
            list2.extend(list1)
        list1 =[]
        list2 = list(set(list2))
        for i in list2:
            list1.append(list(i))
        return list1

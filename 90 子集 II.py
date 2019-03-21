子集 II
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        list2 = []
        for i in range(len(nums)+1):
            list1 = list(itertools.combinations(nums, i))
            list2.extend(list1)
        list1 =[]
        for i in range(len(list2)):
            list2[i] = tuple(sorted(list2[i]))
            # print(list2[i])
        list2 = list(set(list2))
        for i in list2:
            list1.append(list(i))
        return list1

两个数组的交集 II
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        list1 = []
        for i in nums1:
            if i in nums2:
                list1.append(i)
                nums2.pop(nums2.index(i))
        return list1

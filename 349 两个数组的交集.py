两个数组的交集
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums2 = set(nums2) &set(nums1)
        return list(nums2)



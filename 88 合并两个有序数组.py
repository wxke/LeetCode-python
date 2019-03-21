合并两个有序数组
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        cont =0
        for i in nums2:
            nums1.insert(bisect.bisect_left(nums1[:m+cont],i),i)
            nums1.pop()
            cont +=1
        
        

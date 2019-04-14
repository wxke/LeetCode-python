下一个更大元素 I
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if j == len(nums2)-1:
                    nums1[i] = -1
                    break
                if nums2[j] == nums1[i]:
                    for n in range(j+1,len(nums2)):
                        if nums1[i]<nums2[n]:
                            nums1[i] = nums2[n]
                            break
                        elif n == len(nums2)-1:
                            nums1[i]=-1
                    break
        return nums1

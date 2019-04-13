可怜的小猪
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        min1 = (minutesToTest // minutesToDie)+1
        nums1 =0
        t =1
        while t < buckets:
            t = t * min1
            nums1 += 1
        return nums1
        
        

分糖果
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        len1 = len(candies)
        n = len(list(set(candies)))
        if n*2 >= len1: 
            return len1//2
        else :
            return n

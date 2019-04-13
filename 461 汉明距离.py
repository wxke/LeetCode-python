汉明距离
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = x ^y

        sum = 0
        while  x:
            if x%2 ==1:
                sum = sum+1
            x= x>>1
        
        return sum

        

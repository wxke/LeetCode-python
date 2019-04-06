猜数字大小
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        min1 = 0
        max1 = n+1
        while True:
            a = guess( (max1 + min1) //2 )
            
            if a == -1:
                max1 = (max1 + min1) //2
            if a == 1:
                min1 = (max1 + min1) //2
            if a == 0:
                return (max1 + min1) //2
            
                
            

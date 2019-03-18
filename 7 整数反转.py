整数反转
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x= str(x)
        if x[0] == '-':
            x = x[0] + x[:0:-1]
        else:
            x= x[::-1]

        x = int(x)
        if -2**31 < x < 2**31 -1:
            return x
        return 0
        


各位相加
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
#         if num == 0:
#             return 0
        
#         return (num -1)%9 +1
        sum = num
        while sum >=10:
            a = sum
            sum =0
            while a!=0:
                sum =sum + a%10
                a = a//10
        return sum
        

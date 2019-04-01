丑数
class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        if num % 2 == 0:
            num = Solution.isUgly(self,num//2)
        elif num % 3 == 0:
            num = Solution.isUgly(self,num // 3)
        elif num % 5 == 0:
            num = Solution.isUgly(self,num//5)
        if num == 1:
            return True
        else:
            return False

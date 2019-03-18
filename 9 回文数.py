回文数
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        flag = True
        for i in range(0,len(x)):
            j = len(x)-1-i
            if i ==j:
                break;
            if x[i]!= x[j]:
                flag = False
        return flag
        

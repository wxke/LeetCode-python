七进制数
class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        def di(num):
            str1 = ""

            if num // 7 == 0:
                return str(num)
            else:
                str1 += di(num // 7) + str(num % 7)
            return str1
        
        flag = True
        if num < 0:
            num = -num
            flag = False
        str1 = di(num)


        if flag:
            return str1
        else:
            return "-" + str1

数字的补数
class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = bin(num)
        num=num[2:]
        num = list(num)
        for i in range(len(num)):
            if num[i] == '0':
                num[i] ='1'
            else:
                num[i]='0'
        num = "".join(num)

        return int(num,2)


数字转换为十六进制数
class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            return hex(num+4294967296)[2:]
        return hex(num)[2:]

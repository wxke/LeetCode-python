二进制求和
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a,2)
        b = int(b,2)
        a = bin(a+b)

        return a[2:]
        

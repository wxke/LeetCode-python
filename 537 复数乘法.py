复数乘法
class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        first = a.split("+")
        last = b.split("+")
        first[1] = first[1][:-1]
        last[1] = last[1][:-1]
        zhen = int(first[0])*int(last[0]) - int(first[1])*int(last[1])
        fushu = int(first[1])*int(last[0]) + int(first[0])*int(last[1])
        return str(zhen)+"+"+str(fushu)+"i"

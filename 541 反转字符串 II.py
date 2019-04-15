反转字符串 II
class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        j = 1
        str2 = ''
        for i in range(0,len(s),k):
            if j == 1:
                str2 += s[i:i+k][::-1]
                j = 2
            elif j==2:
                str2 += s[i:i+k]
                j = 1


        return str2

Excel表列序号
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        s =s[::-1]
        for i in range(len(s)):
            sum =sum + ( ord(s[i]) - ord('A') + 1 ) * (26**i)
        return sum
        

字符串中的单词数
class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split(" ")
        return len(s) - s.count("")

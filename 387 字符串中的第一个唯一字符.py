字符串中的第一个唯一字符
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        q = list(set(s))
        lis = []
        for i in range(len(q)):
            if s.count(q[i]) == 1:
                lis.append(s.index(q[i]))
        if lis:
            return min(lis)
        else:
            return -1


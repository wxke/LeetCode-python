找不同
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s =list(s)
        t = list(t)
        s.sort()
        t.sort()
        j =0
        s.append(0)
        for i in s:
            if t[j] != i:
                return t[j]
            else:
                j +=1

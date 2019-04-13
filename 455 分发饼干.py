分发饼干
class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        j = 0
        cont = 0
        for i in s:
            if j<len(g) and i >= g[j]:
                j +=1
                cont +=1
        return cont


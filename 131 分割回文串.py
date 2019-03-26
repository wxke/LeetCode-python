分割回文串
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []

        def dp(a, s):
            if s[:] == s[::-1]:
                a.append(s)
                list1 = a[::]
                res.append(list1)
                a.pop()
            for i in range(1,len(s)):
                q = s[:i]
                if q == q[::-1]:
                    a.append(q)
                    dp(a,s[i:])
                    a.pop()
        dp([], s)
        return res
            

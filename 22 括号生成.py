括号生成
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def dp(s ,l,r):
            if len(s) == n*2:
                ans.append(s)
                return
            else:
                if l < n:
                    dp(s+"(",l+1,r)
                if r < l:
                    dp(s+")",l,r+1)
        
        
        dp("",0,0)
        return ans

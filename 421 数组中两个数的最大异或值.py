数组中两个数的最大异或值
class Solution:
    def __init__(self, l=0, r=0):
        self.l = l
        self.r = r

    def findMaximumXOR(self, nums):
        root = Solution()
        for i in nums:
            now = root
            j = 1 << 30
            while j >=1:
                flag = (i & j) > 0
                if flag == 0 and now.l == 0:
                    now.l = Solution()
                elif flag == 1 and now.r == 0:
                    now.r = Solution()
                if flag == 0:
                    now = now.l
                elif flag == 1:
                    now = now.r
                j = j >> 1
        res = 0
        def dfs(a, b, depth, v,res):
            res = max(res, v)
            flag = 0
            if depth == -1:
                return res
            if a.l and b.r:
                res = max(res,dfs(a.l, b.r, depth - 1, v | (1 << depth),res))
                flag = 1
            if a.r and b.l:
                res = max(res,dfs(a.r, b.l, depth - 1, v | (1 << depth),res))
                flag =1
            if flag == 0 and a.l and b.l:
                res = max(res,dfs(a.l, b.l, depth - 1, v,res))
            elif flag == 0 and a.r and b.r:
                res = max(res,dfs(a.r, b.r, depth - 1, v,res))
            return res
        res =dfs(root,root,30,0,res)
        return res

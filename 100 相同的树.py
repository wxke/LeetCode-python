相同的树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.flag = 1
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        def dp(p,q):
            if self.flag == 0:
                return False
            if p != None and q != None:
                if p.val == q.val:
                    dp(p.left,q.left)
                    dp(p.right,q.right)
                else:
                    self.flag =0
                    return False
            elif p != None and q == None:
                self.flag =0
                return False
            elif q != None and p == None:
                self.flag =0
                return False
            return self.flag == 1

        
        return dp(p,q)
                    
        
        

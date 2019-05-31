二叉搜索树的最近公共祖先
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def dp(root,p,q):
            if (root.val - p.val) * (root.val -q.val) <= 0 :
                res = root
                return res
            elif root.val < p.val and root.val < q.val:
                res = dp(root.right,p,q)
            else:
                res = dp(root.left,p,q)
            return res
        return dp(root,p,q)
        

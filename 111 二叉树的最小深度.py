二叉树的最小深度
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        res = []
        if root == None:
            return 0
        def dp(root,ans):
            if root != None and root.left == None and root.right == None:
                res.append(ans+1)
            elif root != None:
                dp(root.left,ans+1)
                dp(root.right,ans+1)

        
        dp(root,0)

        return min(res)

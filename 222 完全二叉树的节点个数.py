完全二叉树的节点个数
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sum1 = 0
    def countNodes(self, root: TreeNode) -> int:
        
        def dp(root):
            if root != None:
                dp(root.left)
                self.sum1 += 1
                dp(root.right)
        
        dp(root)
        return self.sum1
        

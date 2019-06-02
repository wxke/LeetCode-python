左叶子之和
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sum1 = 0
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def dp(root):
            
            if root != None:
                if root.left != None and root.left.left == None and root.left.right == None:
                    self.sum1 += root.left.val
                dp(root.left)
                dp(root.right)
        
        dp(root)
        return self.sum1
        

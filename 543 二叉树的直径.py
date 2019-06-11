二叉树的直径
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        def dp(root):
            if root == None:
                return 0
            else:
                x = dp(root.left)
                y = dp(root.right)
                self.res = max(x+y,self.res)
                return max(x,y) + 1
        
        dp(root)
        return self.res 

平衡二叉树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.flag = True
    def isBalanced(self, root: TreeNode) -> bool:
        res =[]
        if root == None:
            return True
        
        def dp(root):
            if root != None:
                if abs(deep(root.left) - deep(root.right)) >1:
                    self.flag = False
                else:
                    dp(root.left)
                    dp(root.right)
        
        def deep(root):
            if root != None:
                return max(1+deep(root.left),1+deep(root.right))
            else:
                return 0
        dp(root)
        return self.flag
        

        

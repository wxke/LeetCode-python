路径总和
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.flag = 0
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if root == None:
            return False
        def dp(root,res):
            
            if root != None:
                if root.left == None and root.right == None and res-root.val == 0:
                    self.flag = 1
                if root.left != None:
                    dp(root.left,res-root.val)
                if root.right != None:
                    dp(root.right,res-root.val)
        
        dp(root,sum)
        return self.flag == 1
        

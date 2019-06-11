把二叉搜索树转换为累加树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        
        def dp(root):
            if root != None:
                dp(root.right)
                self.res += root.val
                root.val = self.res
                dp(root.left)
        
        dp(root)
        return root
        

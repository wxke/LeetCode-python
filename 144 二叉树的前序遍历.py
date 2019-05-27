二叉树的前序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dp(root):
            if root != None:
                res.append(root.val)
                dp(root.left)
                dp(root.right)
        
        dp(root)
        return res
        

打家劫舍 III
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dp(root):
            if not root:
                return [0,0]
            left = dp(root.left)
            right = dp(root.right)
            res = [left[1]+right[1],max(left[1]+right[1],right[0]+left[0]+root.val)]
            
            return res
        
        return dp(root)[-1]
            
            
        
            
            
        

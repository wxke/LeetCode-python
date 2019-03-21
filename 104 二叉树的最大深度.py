二叉树的最大深度
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: 
            return 0;  
        return 1+max(Solution().maxDepth(root.left), Solution().maxDepth(root.right)); 

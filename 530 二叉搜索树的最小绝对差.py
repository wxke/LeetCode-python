二叉搜索树的最小绝对差
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res = []
        def dp(root):
            if root != None:
                dp(root.left)
                res.append(root.val)
                dp(root.right)
        dp(root)
        import sys
        min1 = sys.maxsize
        for i in range(1,len(res)):
            min1 = min(min1,res[i]-res[i-1])
        
        return min1 
                
        

二叉树中第二小的节点
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res = []
        def dp(root):
            if root != None:
                dp(root.left)
                res.append(root.val)
                dp(root.right)
        dp(root)
        res = list(set(res))
        res = sorted(res)
        print(res)
        return res[1] if len(res) >=2 else -1
        

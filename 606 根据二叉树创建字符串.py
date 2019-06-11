根据二叉树创建字符串
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        
        res = []
        def dp(t):
            if t != None:
                res.append(str(t.val))
                if t.left != None:
                    res.append("(")
                    dp(t.left)
                    res.append(")")

                if t.right != None:
                    if not t.left:
                        res.append("()")
                    res.append("(")
                    dp(t.right)
                    res.append(")")
        dp(t)

        return "".join(res)
            

路径总和 II
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if not root:
            return []
        a = [root.val]
        def dp(root,sum):
            sum = sum - root.val
            if sum == 0 and root.left == None and root.right == None:
                res.append(a[::])
                return
            if root.left != None:
                a.append(root.left.val)
                dp(root.left,sum)
                a.pop()
            if root.right != None:
                a.append(root.right.val)
                dp(root.right,sum)
                a.pop()
        dp(root,sum)
        return res

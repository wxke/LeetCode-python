两数之和 IV - 输入 BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        res = []
        def dp(root):
            if root != None:
                dp(root.left)
                res.append(root.val)
                dp(root.right)
        dp(root)
        dic = {}
        for i in set(res):
            dic[i] = res.count(i)
        

        
        for q in dic.keys():
            dic[q] = dic[q] - 1
            if k - q in dic.keys() and dic[k-q] != 0:
                return True
        
        return False

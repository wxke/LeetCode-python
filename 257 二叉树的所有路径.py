二叉树的所有路径
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root == None:
            return []
        res = []
        def dfs(a,root):
            if root.left == None and root.right == None:
                a += str(root.val)
                res.append(a.strip())
                return 

            
            if root.left != None:
                len1 = 2 + len(str(root.val))
                a += str(root.val)
                a += "->"
                dfs(a,root.left)
                a = a[:-len1]
                
            if root.right != None:
                len1 = 2 + len(str(root.val))
                a += str(root.val)
                a += "->"
                dfs(a,root.right)
                a = a[:-3]
                a = a[:-len1]
                
        dfs("",root)


        return res

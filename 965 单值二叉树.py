单值二叉树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root.left == None and root.right == None:
            return True
            
        import queue
        q = queue.Queue()
        q.put(root)
        flag = root.val
        while q.empty() == False:
            x = q.get()

            if x.val != flag:
                return False
            if x.left != None:
                q.put(x.left)
            if x.right != None:
                q.put(x.right)
 
        
        return True
            
        

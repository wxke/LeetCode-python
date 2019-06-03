找树左下角的值
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        import queue
        q = queue.Queue()
        q.put(root)
        a = queue.Queue()
        left = root.val
        tmp = 1 
        while tmp:
            flag = 0
            while q.empty() == False:
                x = q.get()
                if x.left != None:
                    a.put(x.left)
                    if flag == 0:
                        left = x.left.val
                    flag = 1
                if x.right != None:
                    a.put(x.right)
                    if flag == 0:
                        left = x.right.val
                    flag = 1
            if a.empty():
                tmp = 0
            while a.empty() == False:
                q.put(a.get())
        
        return left
            
                
        

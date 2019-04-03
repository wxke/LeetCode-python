二叉树的层次遍历 II
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        
        ans = [1]
        res = []
        import queue
        q = queue.Queue()
        q.put(root)
        len1 = 1
        a = 0
        while q.empty() == False:
            x = q.get()
            res.append(x.val)
            if len1 > 0:
                if x.left != None:
                    q.put(x.left)
                    a += 1
                if x.right != None:
                    a += 1
                    q.put(x.right)
            len1 -= 1
            if len1 == 0:
                len1 = a
                ans.append(a)
                a = 0

        a = []
        q = []
        for i in ans:
            q= []
            for j in range(0,i):
                q.append(res[0])
                res.pop(0)
            
            a.append(q)
        a.pop()
        return a[::-1]
            
                
            
                
                

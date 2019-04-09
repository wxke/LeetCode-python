N叉树的层序遍历
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        import queue
        q = queue.Queue()
        if root == None:
            return []
        q.put(root)
        ans = [1]
        res = []
        len1 = 1
        a = 0
        
        while q.empty() == False:
            x = q.get()
            
            res.append(x.val)
            if len1 > 0:
                a += len(x.children)
            len1 -= 1
            if len1 == 0:
                ans.append(a)
                len1 = a
                a = 0
            for i in x.children:
                q.put(i)
        

        a = []
        for i in ans:
            q = []
            for j in range(0,i):

                q.append(res[0])
                res.pop(0)
            a.append(q)
        a.pop()
        return a
            
                
        
        
            
            
        
        
        

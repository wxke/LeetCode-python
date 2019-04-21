N叉树的后序遍历
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        list = []
        
        if not root:
            return list
        elif root.children:
            for i in root.children:
                list.append(self.postorder(i))
        list.append(root.val)
            
        lis = []
        for i in range(len(list)):
            if isinstance(list,type(list[i])) :
                for j in range(len(list[i])):
                    lis.append(list[i][j])
            else:
                lis.append(list[i])
        
        return lis
                

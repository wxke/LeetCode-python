N叉树的前序遍历
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        list =[]
        if not root:
            return list
        else:
            list.append(root.val)
            for i in root.children:
                list.extend(self.preorder(i))
        
        return list
                
            

N叉树的最大深度
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        
        if not root :
            return 0
        elif not root.children:
            return 1
        
        return 1 + max(self.maxDepth(child) for child in root.children)
        

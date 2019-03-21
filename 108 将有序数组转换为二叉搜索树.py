将有序数组转换为二叉搜索树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if len(nums) == 0:
            return None
        elif len(nums) ==1:
            return TreeNode(nums[0])
        len1 = len(nums)//2
        root = TreeNode(nums[len1])
       
        if len(nums) == 0:
            return None
        elif len(nums) ==1:
            return root
        
        root.left = self.sortedArrayToBST(nums[:len1])
        root.right = self.sortedArrayToBST(nums[len1 +1:])
        return root
        

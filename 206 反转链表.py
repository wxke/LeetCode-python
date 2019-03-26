反转链表
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a = None

        while head:
            p = head 
            head = head.next
            p.next = a
            a = p
        return a
            
        
        

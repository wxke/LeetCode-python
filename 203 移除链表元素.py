移除链表元素
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return None
        
        top = ListNode(None)
        first = top
        x = head
        while x != None:
            if x.val != val:
                first.next = ListNode(x.val)
                first = first.next
            x = x.next
            
        return top.next

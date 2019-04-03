分隔链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head == None:
            return None
        elif head.next == None:
            return head
        res = ListNode(0)
        y = res
        n = head
        while True:
            if n.val < x:
                y.next = ListNode(n.val)
                y = y.next
            if n.next == None:
                break
            n = n.next
            
        
        n = head
        while True:
            if n.val >= x:
                # print(111)
                y.next = ListNode(n.val)
                y = y.next
            if n.next == None:
                break
            n = n.next
        
        return res.next
        

删除排序链表中的重复元素
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        h = head
        if h == None:
            return []
        while h.next:
            if h.next.val == h.val:
                h.next = h.next.next
            else:
                h = h.next
        
        return head
        

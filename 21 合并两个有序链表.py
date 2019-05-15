合并两个有序链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        x = []
        a = l1
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        while True:
            x.append(a.val)
            if a.next == None:
                break
            else:
                a = a.next
        a = l2
        while True:
            x.append(a.val)
            if a.next == None:
                break
            else:
                a = a.next
        
        x.sort()
        li = ListNode(x[0])
        a = li
        for i in range(1,len(x)):
            a.next = ListNode(x[i])
            a = a.next
        return li

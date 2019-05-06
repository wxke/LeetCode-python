链表的中间结点
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        sum1 = 0
        x = head
        while True:
            sum1 += 1
            if x.next == None:
                break
            else:
                x = x.next
        
        
        if sum1 %2 == 0:
            sum1 += 1
        sum1 = sum1 // 2 
        x = head
        while sum1:
            x = x.next
            sum1 -= 1
        
        return x

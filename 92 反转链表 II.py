反转链表 II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        sum1 = 0
        x = head
        flag = ListNode(0)
        flag.next = head
        res = 0
        while x != None:
            sum1 += 1
            if sum1 == m-1:
                res = 1
                flag = x
                x = x.next 
            elif m <= sum1 < n:
                q = ListNode(x.next.val)
                q.next = flag.next
                flag.next = q
                x.next = x.next.next 
            else:
                x = x.next
            
            
        
        return head if res == 1 else flag.next

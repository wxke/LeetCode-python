两数相加 II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x= l1
        l1_num = 0
        while x.next != None:
            l1_num = l1_num * 10 + x.val
            x = x.next
        l1_num = l1_num * 10 + x.val
        
        y = l2
        l2_num = 0
        while y.next != None:
            l2_num = l2_num * 10 + y.val
            y = y.next
        l2_num = l2_num * 10 + y.val
        
        sum1 = l1_num + l2_num
        len1 = len(str(sum1))
        l3 = ListNode(sum1 // (10**(len1-1)))
        sum1 = sum1 % (10**(len1-1))
        len1 -= 1
        x = l3
        while len1 != 0:
            x.next = ListNode(sum1 // (10**(len1-1)))
            sum1 = sum1 % (10**(len1-1))
            x = x.next
            
            len1 -= 1 
        
        return l3
        
      
        
        

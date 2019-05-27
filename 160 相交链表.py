相交链表
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA ==None or headB == None:
            return None
        res1 = 0
        x = headA
        while x != None:
            x = x.next
            res1 += 1
        
        res2 = 0
        x = headB
        while x != None:
            x = x.next
            res2 += 1
        if res2 >= res1:
            y = headA
            x = headB
            sum1 = res2  - res1
        else:
            y = headB
            x = headA
            sum1 = res1 - res2
        i = 0
        while i < sum1:
            print(1)
            x = x.next
            i+=1

        while x != y:
            x = x.next
            y = y.next
        
        return x

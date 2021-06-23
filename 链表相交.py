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
        size1 = size2 = 0
        cur1, cur2 = headA, headB
        while cur1:
            size1 += 1
            cur1 = cur1.next
        while cur2:
            size2 += 1
            cur2 = cur2.next
        
        if size1 > size2:
            d = size1 - size2
            while d > 0:
                headA = headA.next
                d -= 1
        else:
            d = size2 - size1
            while d > 0:
                headB = headB.next
                d -= 1
        while headA is not None and headB is not None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
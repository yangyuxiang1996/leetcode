#
# @lc app=leetcode.cn id=24 lang=python
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs0(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            tmp = cur.next
            tmp1 = cur.next.next.next

            cur.next = cur.next.next
            cur.next.next = tmp
            tmp.next = tmp1

            cur = tmp

        return dummy.next


    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        递归
        """
        if not head or not head.next:
            return head
        
        # newh = head.next
        # head.next = self.swapPairs(newh.next)
        # newh.next = head
        one = head
        two = head.next
        three = two.next
        
        two.next = one
        one.next = self.swapPairs(three)
        
        return two




# @lc code=end


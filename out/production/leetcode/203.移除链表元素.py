#
# @lc app=leetcode.cn id=203 lang=python
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        # newh = pre = head
        # while newh and newh.val == val:
        #     newh = newh.next
        #     head = head.next

        # while head and head.next:
        #     if head.next.val == val:
        #         head.next = head.next.next
        #     else:
        #         head = head.next
        newh = ListNode(0)
        newh.next = head
        cur = newh
        while cur.next:
            if cur.next == val:
                cur.next = head.next
                head = head.next
            else:
                cur = head
                head = head.next


        return newh.next

# @lc code=end


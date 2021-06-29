#
# @lc app=leetcode.cn id=25 lang=python
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverse(self, a, b):
        # 首先定义反转节点[a, b)之间节点的函数
        pre = None
        cur = a
        while cur != b:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        
        return pre



    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        a, b = head, head
        for i in range(k):
            if b is None:
                return head
            b = b.next

        newh = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return newh       
        

        
        
        


# @lc code=end


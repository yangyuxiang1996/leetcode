#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers0(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        size1, size2 = 0, 0
        cur1, cur2 = l1, l2
        while cur1:
            size1 += 1
            cur1 = cur1.next
        while cur2:
            size2 += 1
            cur2 = cur2.next
        
        if size1 < size2:
            l1, l2 = l2, l1
        
        cur1, cur2 = l1, l2
        flag = 0
        while cur1:
            if cur2:
                cur1.val = cur1.val + cur2.val + flag
                if cur1.val >= 10:
                    flag = 1
                    cur1.val = cur1.val % 10
                else:
                    flag = 0
                cur2 = cur2.next
            else:
                cur1.val = cur1.val + flag
                if cur1.val >= 10:
                    flag = 1
                    cur1.val = cur1.val % 10
                else:
                    flag = 0
            if not cur1.next:
                if flag:
                    cur1.next = ListNode(1)
                    flag = 0
            cur1 = cur1.next
        return l1


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag = 0
        root = cur = ListNode(0)
        while l1 or l2 or flag:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            v = val1 + val2 + flag
            if v >= 10:
                v = v % 10
                flag = 1
            else:
                flag = 0
            cur.next = ListNode(v)
            cur = cur.next
        return root.next
                

# @lc code=end


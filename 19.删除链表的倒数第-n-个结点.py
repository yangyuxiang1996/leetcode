#
# @lc app=leetcode.cn id=19 lang=python
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd0(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next and n > 0:
            return None
        
        cur = head
        size = 0
        while cur:
            size += 1
            cur = cur.next
        
        del_index = size - n
        if del_index == 0:
            return head.next
        else:
            cur = head
            for i in range(1, del_index):
                cur = cur.next
            cur.next = cur.next.next

            return head


    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        双指针，fast先走n步
        """
        if not head:
            return None
        
        fast = slow = head
        for i in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        else:
            while fast and fast.next:
                fast = fast.next
                slow = slow.next
            
            slow.next = slow.next.next
            
            return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    n = 2
    Solution().removeNthFromEnd(head, n)
        

# @lc code=end


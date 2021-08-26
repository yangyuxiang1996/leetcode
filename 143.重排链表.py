#
# @lc app=leetcode.cn id=143 lang=python
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # 先原地讲链表分成两半，然后再反转，再拼接，时间复杂度O(N), 空间复杂度O(1)
        # split
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        # head, mid, 反转mid
        pre = None
        cur = mid
        while cur:
            tmp = cur
            cur = cur.next
            tmp.next = pre
            pre = tmp
        
        # 拼接，head，pre
        cur = head
        while pre:
            tmp = cur.next
            cur.next = pre
            pre = pre.next
            cur.next.next = tmp
            cur = cur.next.next

    def reorderList0(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # 迭代，时间复杂度O(N), 空间复杂度O(N)
        ll = []
        cur = head
        while cur:
            ll.append(cur)
            cur = cur.next

        cur = head
        i, j = 1, len(ll)-1
        while i < j:
            cur.next = ll[j]
            ll[j].next = ll[i]
            cur = ll[i]
            i += 1
            j -= 1
        ll[j].next = None

if __name__ == '__main__':
    head = cur = ListNode(1)
    cur.next = ListNode(2)
    cur.next.next = ListNode(3)
    cur.next.next.next = ListNode(4)

    Solution().reorderList(head)

    while head:
        print(head.val)
        head = head.next
# @lc code=end


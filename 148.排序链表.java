/*
 * @lc app=leetcode.cn id=148 lang=java
 *
 * [148] 排序链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode sortList(ListNode head) {
        // 归并排序
        /*
        找到链表的中点，以中点为分界，将链表拆分成两个子链表。
        寻找链表的中点可以使用快慢指针的做法，快指针每次移动 2 步，慢指针每次移动 1 步，
        当快指针到达链表末尾时，慢指针指向的链表节点即为链表的中点。
        对两个子链表分别排序。
        将两个排序后的子链表合并，得到完整的排序后的链表。
        可以使用「21. 合并两个有序链表」的做法，将两个有序的子链表进行合并。
        */
        return sortFunc(head, null);
        
    }

    public ListNode sortFunc(ListNode head, ListNode tail) {
        if (head == null) {
            return head;
        }
        if (head.next == tail) {
            head.next = null;
            return head;
        }
        ListNode slow = head, fast = head;
        while (fast != tail && fast.next != tail) {
            fast = fast.next.next;
            slow = slow.next;
        }
        ListNode mid = slow;
        return merge(sortFunc(head, mid), sortFunc(mid, tail));
    }

    public ListNode merge(ListNode head1, ListNode head2) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        ListNode l1 = head1;
        ListNode l2 = head2;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) { 
                cur.next = l1;
                l1 = l1.next;
            } else {
                cur.next = l2;
                l2 = l2.next;
            }
            cur = cur.next;
        }
        if (l1 == null) {
            cur.next = l2;
        }
        if (l2 == null) {
            cur.next = l1;
        }
        return dummy.next;
    }

}
// @lc code=end


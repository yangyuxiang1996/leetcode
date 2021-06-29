

/*
 * @Description: 
 * @Author: yangyuxiang
 * @Date: 2021-04-21 23:20:23
 * @LastEditors: yangyuxiang
 * @LastEditTime: 2021-04-21 23:25:57
 * @FilePath: /leetcode/142.环形链表-ii.java
 */
/*
 * @lc app=leetcode.cn id=142 lang=java
 *
 * [142] 环形链表 II
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
class DetectCycle {
    public ListNode detectCycle(ListNode head) {
        
        ListNode fast, slow;
        fast = slow = head;

        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow) {
                slow = head;
                while (fast != slow) {
                    slow = slow.next;
                    fast = fast.next;
                }
                return fast;
            }
        }
        return null;

        
    }
}
// @lc code=end


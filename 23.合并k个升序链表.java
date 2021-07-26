import java.util.PriorityQueue;

/*
 * @lc app=leetcode.cn id=23 lang=java
 *
 * [23] 合并K个升序链表
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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) { 
        if (l1 == null) {
            return l2;
        }
        if (l2 == null) {
            return l1;
        }

        if (l1.val < l2.val) {
            l1.next = mergeTwoLists(l1.next, l2);
        }else {
            l2.next = mergeTwoLists(l1, l2.next);
        }

        return l1.val < l2.val ? l1 : l2;
    }

    public ListNode merge(ListNode[] lists, int l, int r) {
        if (l == r) {
            return lists[l];
        }
        if (l > r) {
            return null;
        }
        int mid = (l + r) / 2;
        return mergeTwoLists(merge(lists, l, mid), merge(lists, mid+1, r));
    }

    public ListNode mergeKLists0(ListNode[] lists) {
        // 分治
        return merge(lists, 0, lists.length-1);
    }

    public ListNode mergeKLists(ListNode[] lists) {
        // 优先队列
        if (lists == null || lists.length == 0) {
            return null;
        }
        PriorityQueue<ListNode> queue = new PriorityQueue<>(lists.length, new Comparator<ListNode>() {
            @Override
            public int compare(ListNode l1, ListNode l2) {
                if (l1.val < l2.val) return -1;
                else if (l1.val == l2.val) return 0;
                else return 1;
            }
        });

        for (ListNode node : lists) {
            if (node != null) queue.add(node);
        }

        ListNode dummy = new ListNode(-1);
        ListNode p = dummy;

        while (!queue.isEmpty()) {
            p.next = queue.poll();
            p = p.next;
            if (p.next != null) {
                queue.add(p.next);
            }
        }
        return dummy.next;
    }
}
// @lc code=end


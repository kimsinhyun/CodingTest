// my solution but only beats 7%
public class Solution {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> set = new HashSet<>();
        boolean cycle = false;
        if (head == null) return false;
        ListNode iter = new ListNode();
        iter.next = head;
        while (iter.next != null) {
            if (!set.contains(iter.next)) {
                set.add(iter.next);
            } else {
                cycle = true;
                break;
            }
            iter = iter.next;
        }
        return cycle;
    }
}

// tortoise and hare solution
// where there are two iterators, one jumps to nodes 
// while the other jumps one, if they meet there is a cycle
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                return true;
            }
        }

        return false;
    }
}
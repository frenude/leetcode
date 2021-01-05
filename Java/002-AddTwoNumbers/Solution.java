import java.util.ArrayList;
import java.util.Arrays;

/**
 * @Author: Frenude
 * @Description: //TODO
 * @Date: Created in 01 05,2021
 * @Modified By:
 **/


public class Solution {

    public static void main(String[] args) {
        ListNode l1 = new ListNode(2, new ListNode(4, new ListNode(3)));
        ListNode l2 = new ListNode(5, new ListNode(6, new ListNode(4)));

        Solution solution = new Solution();
        System.out.println(solution.addTwoNumbers(l1, l2));
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;//进位
        ListNode sum = new ListNode(0);
        ListNode head = sum;
        while ((carry!=0 )|| l1!=null || l2!=null) {
            int val1 = l1 != null ? l1.val : 0 ;
            int val2 = l2 != null ? l2.val : 0 ;
            int r1 = val1 + val2 + carry;
            carry = r1 >= 10 ? 1 : 0;
            sum.next = new ListNode(r1 % 10);
            sum = sum.next ;
            if (l1!=null) l1 = l1.next ;
            if (l2!=null) l2 = l2.next ;
        }
        return head.next;

    }
}

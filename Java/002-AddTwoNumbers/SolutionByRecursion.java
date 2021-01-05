/**
 * @Author: Frenude
 * @Description: //TODO
 * @Date: Created in 01 05,2021
 * @Modified By:
 **/


public class SolutionByRecursion {

    public static void main(String[] args) {
        ListNode l1 = new ListNode(2, new ListNode(4, new ListNode(3)));
        ListNode l2 = new ListNode(5, new ListNode(6, new ListNode(4)));

        SolutionByRecursion solution = new SolutionByRecursion();
        System.out.println(solution.addTwoNumbers(l1, l2));
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode listNode = addTwoNumber(l1, l2, 0);
        return listNode;
    }
    public ListNode addTwoNumber(ListNode l1, ListNode l2 ,int carry){
        if (l1 == null && l2 == null && carry == 0) return null;
        int sum = (l1 != null ? l1.val : 0) + (l2 != null ? l2.val : 0) + carry;
        ListNode node = new ListNode(sum % 10);
        node.next = addTwoNumber(l1 != null ? l1.next : null, l2 != null ? l2.next : null, sum / 10);
        return node;
    }
}

class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode node = head;
        ListNode prev = null;
        ListNode nextIter = null;
        if(node != null && node.next != null)
            head = node.next;
        while(node != null  && node.next != null) {
            nextIter = node.next.next;
            prev = node.next;
            if(prev.next != null && prev.next.next != null)
                node.next=prev.next.next;
            else
                node.next=prev.next;

            prev.next = node;
            node = nextIter;
        }
        return head;
    }
}

//class ListNode {
//    int val;
//    ListNode next;
//    ListNode() {}
//    ListNode(int val) { this.val = val; }
//    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
//}
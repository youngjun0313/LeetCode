//class ListNode {
//    int val;
//    ListNode next;
//
//    ListNode() {
//    }
//
//    ListNode(int val) {
//        this.val = val;
//    }
//
//    ListNode(int val, ListNode next) {
//        this.val = val;
//        this.next = next;
//    }
//}

class Solution1 {

    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length==1)
            return lists[0];
        if(lists.length==0)
            return null;

        ListNode base = lists[0];
        for (int i = 1; i < lists.length; i++)
            base = merge2Lists(base, lists[i]);

        return base;
    }

    private ListNode merge2Lists(ListNode list1, ListNode list2) {
        if(list1==null)
            return list2;
        if(list2==null)
            return list1;

        ListNode head;
        if(list1.val<list2.val) {
            head = list1;
            list1 = list1.next;
        }
        else {
            head = list2;
            list2 = list2.next;
        }


        ListNode pivot = head;
        while(list1!=null && list2!=null) {
            if(list1.val<list2.val) {
                pivot.next = list1;
                pivot = list1;
                list1 = list1.next;
            }
            else {
                pivot.next = list2;
                pivot = list2;
                list2 = list2.next;
            }
        }
        if(list1==null)
            pivot.next = list2;
        else
            pivot.next = list1;

        return head;
    }
}

class Solution2 {

    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length==1)
            return lists[0];
        if(lists.length==0)
            return null;

        ListNode base = lists[0];
        for (int i = 1; i < lists.length; i++)
            base = merge2Lists(base, lists[i]);

        return base;
    }

    private ListNode merge2Lists(ListNode list1, ListNode list2) {
        if(list1==null)
            return list2;
        if(list2==null)
            return list1;

        ListNode head;
        if(list1.val<list2.val) {
            head = list1;
            list1 = list1.next;
        }
        else {
            head = list2;
            list2 = list2.next;
        }


        ListNode pivot = head;
        while(list1!=null && list2!=null) {
            if(list1.val<list2.val) {
                pivot.next = list1;
                pivot = list1;
                list1 = list1.next;
            }
            else {
                pivot.next = list2;
                pivot = list2;
                list2 = list2.next;
            }
        }
        if(list1==null)
            pivot.next = list2;
        else
            pivot.next = list1;

        return head;
    }
}

class Solution3 {
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length==1)
            return lists[0];

        if(lists.length==0)
            return null;

        return partition(lists, 0, lists.length-1);
    }

    private ListNode partition(ListNode[] lists, int i, int j) {
        if(i==j)
            return lists[i];

        int pivot = (i+j)/2;

        ListNode node1 = partition(lists, i, pivot);
        ListNode node2 = partition(lists, pivot+1, j);
        return merge2Lists(node1, node2);
    }

    private ListNode merge2Lists(ListNode list1, ListNode list2) {
        if(list1==null)
            return list2;
        if(list2==null)
            return list1;

        ListNode head;
        if(list1.val<list2.val) {
            head = list1;
            list1 = list1.next;
        }
        else {
            head = list2;
            list2 = list2.next;
        }


        ListNode pivot = head;
        while(list1!=null && list2!=null) {
            if(list1.val<list2.val) {
                pivot.next = list1;
                pivot = list1;
                list1 = list1.next;
            }
            else {
                pivot.next = list2;
                pivot = list2;
                list2 = list2.next;
            }
        }
        if(list1==null)
            pivot.next = list2;
        else
            pivot.next = list1;

        return head;
    }
}
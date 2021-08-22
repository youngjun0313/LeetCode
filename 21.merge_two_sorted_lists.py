# Definition for singly-linked list.
from typing import *
import copy
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if(l1 == None and l2 != None):
            return l2
        elif(l1 != None and l2 == None):
            return l1
        elif(l1 == None and l2 == None):
            return None
        else:
            p = l1
            q = l2
            head = None
            if(p.val < q.val):
                head = ListNode(val = p.val)
                ans = head
                p = p.next
            else:
                head = ListNode(val = q.val)
                ans = head 
                q = q.next
            while(p != None or q != None):
                if(p == None):
                    head.next = q
                    break
                elif(q == None):
                    head.next = p
                    break
                else:
                    if(p.val < q.val):
                        head.next = p
                        p = p.next
                        head = head.next
                    else:
                        head.next = q
                        q = q.next
                        head = head.next
        return ans

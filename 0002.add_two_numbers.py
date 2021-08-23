import copy
from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def makeNode(val: int) -> Optional[ListNode]:
        if(val == 0):
            return None
        return ListNode(val%10, makeNode(val // 10))

    def loop(l1: Optional[ListNode], l2: Optional[ListNode], digit:int, ans: int) -> int:
        if(l1 == None and l2 == None):
            return ans
        else:
            if(l1 == None):
                return loop(None, l2.next, digit*10, ans + l2.val*digit)
            elif(l2 == None):
                return loop(l1.next, None, digit*10, ans + l1.val*digit)
            else:
                return loop(l1.next, l2.next, digit*10, ans + l1.val*digit + l2.val*digit)
            
    arg = loop(l1, l2, 1, 0)
    if(arg == 0):
        return ListNode(0)

    return makeNode(arg)
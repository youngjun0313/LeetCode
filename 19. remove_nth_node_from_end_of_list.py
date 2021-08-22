# Definition for singly-linked list.
from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodeList = []
        nodeLen = 0
        node = head
        while(node != None):
            nodeList.append(node)
            node = node.next
            nodeLen = nodeLen + 1
        if(nodeLen-n-1 < 0):
            return nodeList[nodeLen-n]
        nodeList[nodeLen-n-1].next = nodeList[nodeLen-n+1]
        
        return head


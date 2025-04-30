from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Remove the nth node from the end of the list 
        Args:
            head (ListNode): Head of the linked list.
            n (int): Position from the end (1-indexed) to be removed.
        Returns:
            head of modified linked list
        '''
        dummy=ListNode()
        dummy.next=head
        fast=dummy
        slow=dummy

        for i in range(n):
            fast=fast.next # type: ignore

        while fast and fast.next:
            fast=fast.next
            slow=slow.next # type: ignore
        slow.next=slow.next.next # type: ignore

        return dummy.next
        
        
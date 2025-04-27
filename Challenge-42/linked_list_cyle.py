# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        Determine if a linked list has a cycle.

        Args:
            head: The head node of the linked list.

        Returns:
            True if there is a cycle, False otherwise.
        '''
        slow=head
        fast=head
        while fast and fast.next:            
            slow=slow.next # type: ignore
            fast=fast.next.next
            if slow==fast:
                return True
        return False
        
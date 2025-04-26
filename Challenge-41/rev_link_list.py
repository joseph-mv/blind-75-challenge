# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Reverse a singly linked list.

        Args:
            head: The head of the singly linked list.

        Returns:
            ListNode: The head of the reversed linked list.
        '''
        if not head or not head.next:
            return head

        pre_prev=None
        prev=head
        current=head.next
        while prev:
            prev.next=pre_prev
            pre_prev=prev
            prev=current
            if current:
                current=current.next

        return pre_prev

        
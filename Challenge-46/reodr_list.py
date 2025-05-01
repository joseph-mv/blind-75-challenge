from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Modify the singly linked list in-place to reorder it as:
        L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
        Args:
            head:head of singly Linked list.
            
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next # type: ignore
        while fast and fast.next :
            fast=fast.next.next
            slow=slow.next # type: ignore

        part2=slow.next # type: ignore
        slow.next=None       # type: ignore

        def reverse(head):
            if not head or not head.next:
                return head
            pre_prev, prev = None, head
            current=head.next

            while prev:
                prev.next=pre_prev
                pre_prev=prev
                prev=current
                if current:
                    current=current.next          
            return pre_prev

        first,second=head,reverse(part2)

        while second:
            tmp1, tmp2 = first.next, second.next # type: ignore
            first.next=second # type: ignore
            second.next=tmp1
            first, second = tmp1, tmp2
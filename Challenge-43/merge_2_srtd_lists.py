from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Merge the two sorted lists into one sorted list.
        Args:
            list1 and list2: Two sorted linked lists
        Returns:
            The head of the merged linked list.
        '''
        dummy=ListNode()
        current=dummy
        
        while list1 and list2:
            if list1.val<list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            current=current.next

        current.next=list1 or list2
        return dummy.next
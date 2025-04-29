from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        Merge K sorted linked lists into one sorted linked-list
        Args:
            lists:An array of k linked-lists
        Returns:
            One sorted linked-list
        '''
       
        def merge2lists(list1,list2):
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

        def merge_sort(lists):
            l=len(lists)
            if l==0:
                return
            if l==1:
                return lists[0]

            list1=merge_sort(lists[:l//2])
            list2=merge_sort(lists[l//2:])
            return merge2lists(list1,list2)

        return merge_sort(lists)
# Approach-1 : What i thought is to swap the values only of pair wise nodes


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        ptr=head
        while ptr and ptr.next:
            ptr.val, ptr.next.val = ptr.next.val, ptr.val
            ptr=ptr.next.next
        return head
        
     

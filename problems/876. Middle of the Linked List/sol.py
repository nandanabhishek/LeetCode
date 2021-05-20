# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        tortoise=head
        hare=head
        
        if head.next is None:
            return head
        while hare and hare.next:
            tortoise=tortoise.next
            hare=hare.next.next
        return tortoise
        
        
        # Important Technique !!!
        # If object 1 is moving at speed of 2x and object2 at speed of x than object2 will be on halfway when the object1 complete the distance.

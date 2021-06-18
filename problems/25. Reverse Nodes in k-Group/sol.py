# also try to get its Iterative Solution


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Recursive Solution !
        
        if head is None or k < 2:
            return head
    
        ptr = head
        
        for i in range(k - 1):
            ptr = ptr.next
            if ptr is None:
                return head

        # for reversing the linked list till size k
        prev = None
        current =  head
        for i in range(k):
            next = current.next
            current.next = prev
            prev = current
            current = next

        head.next = self.reverseKGroup(current, k)

        return prev
        
      

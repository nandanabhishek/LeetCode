# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # base case 
        if head==None or head.next==None:
            return head
        
        curr = head
        while curr.next!=None:
            if curr.val==curr.next.val:
                temp=curr.next  # this line can be avoided also
                curr.next = curr.next.next
                temp.next=None # this line also can be avoided
            else:
                curr = curr.next
        return head
        

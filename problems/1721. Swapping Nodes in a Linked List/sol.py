# Approach-1: What I thought - Only values of nodes are swapped here


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        # when linked list has 0 or 1 node
        if head==None or head.next==None: 
            return head
        
        first=head
        last=head
        
        temp=head
        
        # for getting first pointer at source node
        for i in range(1, k):
            first=first.next
        
        # for getting last pointer at destination node
        # it's somewhat working like sliding window by using this we don't need to count total number of elements in linked list !!!!!!
        temp=first
        while temp.next:
            last=last.next
            temp=temp.next   
            
        # for swapping the values of source and destination node
        first.val, last.val = last.val, first.val
        
        return head
            
            
            
            
        

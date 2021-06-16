# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # base case
        if head is None or head.next is None:
            return head
        
        # get the middle of linked list
        middle = self.getMiddle(head)
        nextToMiddle = middle.next
        
        # so that one linked list is divided into 2 parts
        middle.next = None
        
        # apply merge sort on left & right sub-list
        left = self.sortList(head)
        right = self.sortList(nextToMiddle)
        
        # merge the sorted left and right sub-lists
        sortedList=self.mergeSortedList(left, right)
        
        return sortedList
            
        
    def mergeSortedList(self, first, second):
        
        # Base cases
        if not first:
            return second
        
        if not second:
            return first
        
        res = None
        
        if first.val <= second.val:
            res = first
            res.next = self.mergeSortedList(first.next, second)
            
        else:
            res=second
            res.next = self.mergeSortedList(first, second.next)
            
        return res
    
            
    # function to get the middle of linked list   
    def getMiddle(self, head):
        
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
            
        
        

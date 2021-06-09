# Approach - 1: What I thought


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        a=[]  # this will use memeory O(n)
        while head:
            a.append(head.val)
            head=head.next
        return a==a[::-1]
    
    # Time complexity : O(n)
    # Space Complexity : O(n)
        
      
      
      
# Approach - 2: With O(n) time and O(n) space

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # base case
        if head==None or head.next==None:
            return True
        
        a=[] # we will use this as a stack 
        ptr=head
        while ptr:
            a.append(ptr.val)
            ptr=ptr.next
        
        ispalin=True
        while head:
            
            if head.val==a.pop():
                ispalin=True
            else:
                ispalin=False
                break
            
            head=head.next
        return ispalin
    
    
    

# Approach - 3: with O(n) time and O(1) space
            # Reverse second half of linked list  !!!! Best approach
    
    
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        fast = slow = head
        
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # reverse the second half
        curr=slow
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # compare the first and second half nodes
        
        while prev: # while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
            
        return True
        
        
            
            
    
    
        

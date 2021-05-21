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
        
      
      
      
# Approach - 2: With O(n) time and O(1) space
